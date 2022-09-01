"""Users Wish module."""
import logging

from flask import request

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Resource
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource


from Library.blueprints.users.actions import create_wish_entry, delete_wish_entry
from Library.blueprints.users.serializers import wish
from Library.blueprints.blueprint import api
from Library.models.models import Wish


log = logging.getLogger(__name__)

ns = api.namespace('users/wish', description='Users Wishlist namespace')


def get_users_wishlist(user_id):
    """
    Get users wishlist.

    :param user_id:
    :return:
    """
    return_response = Wish.query.filter(
        Wish.user_id == user_id
    ).all()
    return (return_response, 200) if len(return_response) > 0 else (return_response, 204)


@ns.route('/wish_add')
class WishAdd(Resource):
    """Class to add a Wish."""

    @api.response(201, 'Wish successfully created.')
    @api.expect(wish)
    def post(self):
        """Create a new Wish."""
        data = request.json
        return create_wish_entry(data=data)


@ns.route('/wish_delete/<int:book_id>/<int:user_id>')
@api.response(404, 'Book not found on the wishlist.')
class WishDelete(Resource):
    """Class to delete a wish."""

    @api.response(204, 'Book successfully removed from your wishlist.')
    def delete(self, book_id, user_id):
        """Delete the book from your wishlist."""
        return delete_wish_entry(book_id=book_id, user_id=user_id)


@ns.route('/wishlist/<string:user_id>')
@api.response(404, 'Wishlist not found. Server Error')
@api.response(204, 'Wishlist is empty.')
class UserWishlist(Resource):
    """Class to list all the wishes for the user."""

    @api.marshal_with(wish)
    def get(self, user_id):
        """Return the user's wishlist."""
        return get_users_wishlist(user_id=user_id)

