"""Flask Restplus app module"""
import logging.config

import os
from waitress import serve
from flask import Flask, Blueprint
from DGBMICalculator import settings
from DGBMICalculator.blueprints.bmi.endpoints.bmi import ns as bmi_categories_namespace
from DGBMICalculator.blueprints.bmi.endpoints.search import ns as bmi_category_search_namespace
from DGBMICalculator.blueprints.bmi.endpoints.calculate import ns as bmi_calculate_namespace
from DGBMICalculator.blueprints.blueprint import api
from DGBMICalculator.models import db

LOGGING_CONF_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(LOGGING_CONF_PATH)
LOG = logging.getLogger(__name__)


class BMIServer:
    """Class representing flask-restplus server for BMI"""
    def __init__(self, config_level='prod'):
        """Constructor"""
        self.app = Flask(__name__)
        self.setting = settings.CONFIG_BY_NAME[config_level]

    def configure_app(self, flask_app):
        """app configuration method"""
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
        """app initialization method"""
        self.configure_app(flask_app)

        blueprint = Blueprint('api', __name__, url_prefix='/api')
        api.init_app(blueprint)
        api.add_namespace(bmi_categories_namespace)
        api.add_namespace(bmi_category_search_namespace)
        api.add_namespace(bmi_calculate_namespace)
        flask_app.register_blueprint(blueprint)

        db.init_app(flask_app)

    def main(self):
        """app main execution method"""
        self.initialize_app(self.app)
        LOG.info(f'Starting flask server at http://{self.app.config["SERVER_NAME"]}/api/')
        serve(
            self.app,
            host=self.setting.FLASK_SERVER_NAME,
            port=self.setting.FLASK_SERVER_PORT
        )


BMI_SERVER = BMIServer()
BMI_SERVER.main()
