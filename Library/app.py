"""Flask Restplus app module for Library."""
import logging.config

import os
from waitress import serve
from flask import Flask, Blueprint
from Library import settings
from Library.blueprints.users.endpoints.search import ns as users_search_namespace
from Library.blueprints.users.endpoints.wish import ns as users_wish_namespace
from Library.blueprints.staff.endpoints.search import ns as staff_search_namespace
from Library.blueprints.staff.endpoints.admin import ns as staff_admin_namespace
from Library.blueprints.blueprint import api
from Library.models import db

LOGGING_CONF_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(LOGGING_CONF_PATH)
LOG = logging.getLogger(__name__)


class LibraryServer:
    """Class representing flask-restplus server for LIBRARY."""

    def __init__(self, config_level='prod'):
        """Initialize or Construct."""
        self.app = Flask(__name__)
        self.setting = settings.CONFIG_BY_NAME[config_level]

    def configure_app(self, flask_app):
        """App configuration method."""
        flask_app.config['SERVER_NAME'] = self.setting.FLASK_SERVER_NAME + \
                                          ':' + str(self.setting.FLASK_SERVER_PORT)
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = self.setting.SQLALCHEMY_DATABASE_URI
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
            self.setting.SQLALCHEMY_TRACK_MODIFICATIONS
        flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = \
            self.setting.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
        flask_app.config['RESTPLUS_VALIDATE'] = self.setting.RESTPLUS_VALIDATE
        flask_app.config['RESTPLUS_MASK_SWAGGER'] = self.setting.RESTPLUS_MASK_SWAGGER
        flask_app.config['ERROR_404_HELP'] = self.setting.RESTPLUS_ERROR_404_HELP

    def initialize_app(self, flask_app):
        """App initialization method."""
        self.configure_app(flask_app)

        blueprint = Blueprint('api', __name__, url_prefix='/api')
        api.init_app(blueprint)
        api.add_namespace(users_search_namespace)
        api.add_namespace(users_wish_namespace)
        api.add_namespace(staff_search_namespace)
        api.add_namespace(staff_admin_namespace)
        flask_app.register_blueprint(blueprint)

        db.init_app(flask_app)

    def main(self):
        """App main execution method."""
        self.initialize_app(self.app)
        LOG.info(f'Starting flask server at http://{self.app.config["SERVER_NAME"]}/api/')
        serve(
            self.app,
            host=self.setting.FLASK_SERVER_NAME,
            port=self.setting.FLASK_SERVER_PORT
        )


LIBRARY_SERVER = LibraryServer()
LIBRARY_SERVER.main()
