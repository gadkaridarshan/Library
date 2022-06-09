import logging
import traceback

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Api
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Api

from DGBMICalculator import settings
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

api = Api(version='1.0', title='BMI Calculator API',
          description='BMI Calculator API built by Darshan Gadkari')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    """No results found in database"""
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404

