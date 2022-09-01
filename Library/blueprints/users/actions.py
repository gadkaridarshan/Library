"""Users Actions module."""
from Library.models import db
from Library.models.models import Book, Wish, User
from sqlalchemy.orm.exc import NoResultFound
import logging


def search_if_book_already_on_the_user_wishlist(book_id, user_id):
    """
    Check to see if the book is already on the user's wishlist.

    :param book_id:
    :param user_id:
    :return: Book model
    """
    logging.debug(f"book_id: {book_id}")
    logging.debug(f"user_id: {user_id}")
    return_response = Wish.query.filter(
        Wish.book_id == book_id,
        Wish.user_id == user_id
    ).all()
    logging.debug(f"return_response: {return_response}")
    return return_response


def create_wish_entry(data):
    """
    Create entry for a wish.

    :param data:
    :return:
    """
    try:
        # check if the user with user_id exists
        logging.debug(f"book_id: {data.get('book_id')}")
        logging.debug(f"user_id: {data.get('user_id')}")
        return_response = User.query.filter(
            User.id == data.get('user_id')
        ).one()
        logging.debug(f"return_response: {return_response}")
    except NoResultFound as nrf:
        return {
                   "Msg": f"The user with the user_id {data.get('user_id')} does not exist",
                   "Status": "Failure to add to the Wishlist"
               }, 404

    try:
        # check if the book with book id exists
        return_response = Book.query.filter(
            Book.book_id == data.get('book_id')
        ).one()
        logging.debug(f"return_response: {return_response}")
    except NoResultFound as nrf:
        return {
                   "Msg": f"The book with the book_id {data.get('book_id')} does not exist",
                   "Status": "Failure to add to the Wishlist"
               }, 404

    try:
        # check if the book with book id is available or borrowed
        return_response = Book.query.filter(
            Book.book_id == data.get('book_id'),
            Book.book_availability == 'Borrowed'
        ).one()
        logging.debug(f"return_response: {return_response}")
    except NoResultFound as nrf:
        return {
                   "Msg": f"The book with the book_id {data.get('book_id')} is already available for pickup",
                   "Status": "Declined to be added to the Wishlist"
               }, 404

    # check if the user has already put the book on her/his wishlist
    if len(search_if_book_already_on_the_user_wishlist(book_id=data.get('book_id'), user_id=data.get('user_id'))):
        return {
                   "Error Msg": f"The book with the book_id {data.get('book_id')} is already on your wishlist",
                   "Status": "Failure to add to the Wishlist"
               }, 404

    try:
        # insert a record for the user's wish
        wish = Wish(
            book_id=data.get('book_id'),
            user_id=data.get('user_id')
        )

        db.session.add(wish)
        db.session.commit()
        return {
                   "Msg": f"The book with the book_id {data.get('book_id')} has been added to your wishlist",
                   "Status": "Successfully added to your Wishlist"
               }, 201
    except Exception as e:
        # rollback on exception
        db.session.rollback()
        return {
                   "Msg": f"The book with the book_id {data.get('book_id')} has NOT been added to your wishlist",
                   "Error": f"{e}",
                   "Status": "Unable to add to your Wishlist"
               }, 404


def delete_wish_entry(book_id, user_id):
    """
    Delete an existing wish.

    :param book_id:
    :param user_id:
    :return:
    """
    try:
        wish = Wish.query.filter(
            Wish.book_id == book_id,
            Wish.user_id == user_id
        ).one()
        db.session.delete(wish)
        db.session.commit()
        return {
                   "Msg": f"The book with the book_id {book_id} has been removed from your wishlist",
                   "Status": "Success"
               }, 201
    except NoResultFound as nrf:
        # rollback on exception
        db.session.rollback()
        return {
                   "Error Msg": f"The book with the book_id {book_id} is not on your wishlist",
                   "Status": "Failure"
               }, 404
