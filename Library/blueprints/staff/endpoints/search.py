"""Staff Search module."""
import logging


import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Resource
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource

from Library.blueprints.staff.serializers import all_users, all_wishes
from Library.blueprints.blueprint import api
from Library.models.models import User, Wish


log = logging.getLogger(__name__)

ns = api.namespace('staff/search', description='Staff Search namespace')


def get_all_users():
    """
    Get all users.

    :return:
    """
    return_response = User.query.filter().all()
    return (return_response, 200) if len(return_response) > 0 else (return_response, 204)


def get_entire_wishlist():
    """
    Get entire wishlist for all users.

    :return:
    """
    return_response = Wish.query.filter().all()
    return (return_response, 200) if len(return_response) > 0 else (return_response, 204)


@ns.route('/all_users')
@api.response(404, 'User not found. Server Error')
@api.response(204, 'No User found.')
class AllUsers(Resource):
    """Class to list all users."""

    @api.marshal_with(all_users)
    def get(self):
        """Return a specific Book."""
        return get_all_users()


@ns.route('/wishlist')
@api.response(404, 'Wishlist not found. Server Error')
@api.response(204, 'Wishlist is empty.')
class Wishlist(Resource):
    """Class to list all wishes for all users."""

    @api.marshal_with(all_wishes)
    def get(self):
        """Return a specific Book."""
        return get_entire_wishlist()

