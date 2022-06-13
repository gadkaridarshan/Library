"""Flask Restplus Blueprint module"""
import logging
from sqlalchemy.orm.exc import NoResultFound

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Api
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Api

LOG = logging.getLogger(__name__)

api = Api(version='1.0', title='BMI Calculator API',
          description='BMI Calculator API built by Darshan Gadkari')


@api.errorhandler
def default_error_handler(e):
    """Function: Handles default errors"""
    message = 'An unhandled exception occurred.'
    LOG.exception(f'message. {message}. {e}')
    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    """Function: No results found in database"""
    LOG.warning(f'A database record was not found. {e}')
    return {'message': 'A database record was not found.'}, 404
