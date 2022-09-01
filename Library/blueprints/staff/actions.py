"""Staff Actions module."""
import logging
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from os import getcwd, pardir, path
from requests import get
from time import sleep

from Library.models import db
from Library.models.models import Book, Wish, User
from sqlalchemy.orm.exc import NoResultFound
from Library import settings


def get_engine():
    """
    Get engine.

    :return:
    """
    setting = settings.CONFIG_BY_NAME['prod']
    return create_engine(setting.SQLALCHEMY_DATABASE_URI)


def update_book_availability_status_to_borrowed(book_id):
    """
    Update book availability to borrowed.

    :param book_id:
    :return:
    """
    try:
        # check if the book with book_id exists
        logging.debug(f"book_id: {book_id}")
        book = Book.query.filter(
            Book.book_id == book_id
        ).one()
        logging.debug(f"return_response: {book}")
    except NoResultFound as nrf:
        return {
                   "Msg": f"The book with the book_id {book_id} does not exist",
                   "Status": "Failure"
               }, 404

    # check if the book with book id is available or borrowed
    if book.book_availability == 'Borrowed':
        return {
                   "Msg": f"The book with the book_id {book_id} is already borrowed",
                   "Status": "Declined to update the availability"
               }, 404

    try:
        # update book_availability from Available to Borrowed
        book.book_availability = "Borrowed"
        book.rented_at = datetime.utcnow()
        db.session.add(book)
        db.session.commit()

        return {
                   "Msg": f"The book with the book_id {book_id} is now in Borrowed status",
                   "Status": "Successfully updated availability to Borrowed"
               }, 201
    except Exception as e:
        # rollback on exception
        db.session.rollback()
        return {
                   "Msg": f"The book with the book_id {book_id} is still in Available status",
                   "Error": f"{e}",
                   "Status": "Unable to update status"
               }, 404


def update_book_availability_status_to_available(book_id):
    """
    Update book availability to available.

    :param book_id:
    :return:
    """
    try:
        # check if the book with book_id exists
        logging.debug(f"book_id: {book_id}")
        book = Book.query.filter(
            Book.book_id == book_id
        ).one()
        logging.debug(f"return_response: {book}")
    except NoResultFound as nrf:
        return {
                   "Msg": f"The book with the book_id {book_id} does not exist",
                   "Status": "Failure"
               }, 404

    # check if the book with book id is available or borrowed
    if book.book_availability == 'Available':
        return {
                   "Msg": f"The book with the book_id {book_id} is already available for pickup",
                   "Status": "Declined to update the availability"
               }, 404

    try:
        # update book_availability from Borrowed to Available
        book.book_availability = "Available"
        db.session.add(book)

        # find all the entries in the Wish table related to the book_id
        wishes = Wish.query.filter(
            Wish.book_id == book_id
        ).all()

        # remove all the entries in the Wish table related to the book_id
        for wish in wishes:
            # get first name and last name of the users who wished for this book
            user = User.query.filter(
                User.id == wish.user_id
            ).one()
            # send fake email to the users based on the user_id
            logging.debug(f"Email to user_id {wish.user_id} that the book is now available")
            logging.debug(f"First name: {user.first_name} Last name: {user.last_name}")
            db.session.delete(wish)

        db.session.commit()

        return {
                   "Msg": f"The book with the book_id {book_id} is now in Available status",
                   "Status": "Successfully updated availability to Available"
               }, 201
    except Exception as e:
        # rollback on exception
        db.session.rollback()
        return {
                   "Msg": f"The book with the book_id {book_id} is still in Borrowed status",
                   "Error": f"{e}",
                   "Status": "Unable to update status"
               }, 404


def get_rented_report():
    """
    Get rented report.

    :return:
    """
    try:
        # get the list of books that are in Borrowed status
        books = Book.query.filter(
            Book.book_availability == 'Borrowed'
        ).all()
        for book in books:
            rented_for = (
                    datetime.utcnow() - book.rented_at
            )
            book.rented_for_in_days = rented_for.days
            book.rented_for_in_seconds = rented_for.seconds
        logging.debug(f"return_response: {books}")
        return books, 201
    except NoResultFound as nrf:
        return {
                   "Msg": "No books are currently rented/borrowed",
                   "Status": "Success"
               }, 404


def load_books_data():
    """
    Load books data.

    :return:
    """
    # location of the books data file
    data_folder = path.abspath(path.join(getcwd(), pardir))
    data_folder = data_folder + '/Library/data/'
    books_data_file = data_folder + 'Backend Data.csv'
    logging.debug(books_data_file)

    # truncate the Wish table
    db.session.execute('''DELETE FROM Wish''')

    # truncate the Book table
    db.session.execute('''DELETE FROM Book''')

    db.session.commit()

    # get connection / engine
    e = get_engine()

    df_books = pd.read_csv(books_data_file)

    logging.debug(len(df_books))

    df_books.rename(columns={
        'Id': 'book_id',
        'ISBN': 'book_ISBN',
        'Authors': 'book_authors',
        'Publication Year': 'book_publication_year',
        'Title': 'book_title',
        'Language': 'book_language'
    }, inplace=True)

    df_books['book_availability'] = 'Available'
    df_books['created_at'] = datetime.utcnow()
    df_books['created_at'] = df_books['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S.%f')
    df_books['rented_at'] = df_books['created_at']

    # df_books.index.name = 'id'
    logging.debug(df_books.head())
    logging.debug(df_books.dtypes)

    try:
        df_books.to_sql('Book', con=e, if_exists='append', index=False)
        print('Books Data Load: Done')
    except Exception as e:
        logging.error(e)


def get_amazon_id(amazon_url):
    """
    Get amazon id.

    :param amazon_url:
    :return:
    """
    sleep(1)
    logging.debug(amazon_url)
    response = get(amazon_url)
    if 200 <= response.status_code < 300:
        logging.debug(response.json()['key'].split('/books/')[1])
        return response.json()['key'].split('/books/')[1]
    else:
        return 'NA'


def populate_amazon_url_id():
    """Populate amazon url id."""
    # get connection / engine
    e = get_engine()

    # create pandas dataframe from the Books table
    df_books = pd.read_sql(Book.query.filter().statement, con=e)

    df_books['amazon_url'] = 'https://openlibrary.org/isbn/' + df_books['book_ISBN'] + '.json'
    logging.debug(df_books.tail())

    df_books['amazon_id'] = df_books['amazon_url'].apply(get_amazon_id)

    logging.debug(df_books[['amazon_url', 'amazon_id']])

    # truncate the Book table
    db.session.execute('''DELETE FROM Book''')

    db.session.commit()

    try:
        df_books.to_sql('Book', con=e, if_exists='append', index=False)
        print('Books Data Load: Done')
    except Exception as e:
        logging.error(e)


