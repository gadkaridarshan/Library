"""Users Search module."""
import logging


import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Resource
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource

from Library.blueprints.users.serializers import book_search
from Library.blueprints.blueprint import api
from Library.models.models import Book


log = logging.getLogger(__name__)

ns = api.namespace('users/search', description='User Search namespace')


def search_book_by_title(book_title):
    """
    Search book by title.

    :param book_title:
    :return:
    """
    return_response = Book.query.filter(
        Book.book_title.contains(book_title)
    ).all()
    logging.debug(return_response)
    return (return_response, 200) if len(return_response) > 0 else (return_response, 204)


def search_book_by_author(book_author):
    """
    Search book by author.

    :param book_author:
    :return:
    """
    return_response = Book.query.filter(
        Book.book_authors.contains(book_author)
    ).all()
    logging.debug(return_response)
    return (return_response, 200) if len(return_response) > 0 else (return_response, 204)


def search_book_by_title_and_author(book_title, book_author):
    """
    Search book by title and author.

    :param book_title:
    :param book_author:
    :return:
    """
    return_response = Book.query.filter(
        Book.book_title.contains(book_title),
        Book.book_authors.contains(book_author)
    ).all()
    logging.debug(return_response)
    return (return_response, 200) if len(return_response) > 0 else (return_response, 204)


@ns.route('/search_by_title/<string:book_title>')
@api.response(404, 'Book not found. Server Error')
@api.response(204, 'No Book found.')
class BookSearchByTitle(Resource):
    """Class for Searching by Title."""

    @api.marshal_with(book_search)
    def get(self, book_title):
        """Return a specific Book."""
        logging.debug(f'Book Title: {book_title}')
        return search_book_by_title(book_title=book_title)


@ns.route('/search_by_author/<string:book_author>')
@api.response(404, 'Book not found. Server Error')
@api.response(204, 'No Book found.')
class BookSearchByAuthor(Resource):
    """Class for Searching by Author."""

    @api.marshal_with(book_search)
    def get(self, book_author):
        """Return a specific Book."""
        logging.debug(f'Book Author: {book_author}')
        return search_book_by_author(book_author=book_author)


@ns.route('/search_by_title_and_author/<string:book_title>/<string:book_author>')
@api.response(404, 'Book not found. Server Error')
@api.response(204, 'No Book found.')
class BookSearchByTitleAndAuthor(Resource):
    """Class for Searching by Title and Author."""

    @api.marshal_with(book_search)
    def get(self, book_title, book_author):
        """Return a specific Book."""
        logging.debug(f'Book Title: {book_title}, Book Author: {book_author}')
        return search_book_by_title_and_author(book_title=book_title, book_author=book_author)

