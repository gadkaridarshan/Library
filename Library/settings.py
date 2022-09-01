"""Settings module."""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Class representing a configuration for flask-restplus."""

    DEBUG = False

    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    def get_debug_value(self):
        """Return DEBUG config value."""
        return self.DEBUG

    def get_restplus_swagger_ui_doc_expansion_value(self):
        """Return RESTPLUS_SWAGGER_UI_DOC_EXPANSION config value."""
        return self.RESTPLUS_SWAGGER_UI_DOC_EXPANSION

    def get_restplus_validate_value(self):
        """Return RESTPLUS_VALIDATE config value."""
        return self.RESTPLUS_VALIDATE

    def get_restplus_error_404_help_value(self):
        """Return RESTPLUS_ERROR_404_HELP config value."""
        return self.RESTPLUS_ERROR_404_HELP


class DevelopmentConfig(Config):
    """
    # Development level configurations.

    # For now all configurations (Dev, Test and Prod) are the same
    """

    # Flask settings
    FLASK_SERVER_NAME = 'localhost'
    FLASK_SERVER_PORT = 8888

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/darshangadkari/Documents/FCA/Library/db.sqlite'
    SQLALCHEMY_DATABASE_URI_EMPTY = 'sqlite:////Users/darshangadkari/Documents/FCA/Library/db_empty.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    # Development level configurations.

    # For now all configurations (Dev, Test and Prod) are the same
    """

    # Flask settings
    FLASK_SERVER_NAME = 'localhost'
    FLASK_SERVER_PORT = 8888

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/darshangadkari/Documents/FCA/Library/db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    # Development level configurations.

    # For now all configurations (Dev, Test and Prod) are the same
    """

    # Flask settings
    FLASK_SERVER_NAME = 'localhost'
    FLASK_SERVER_PORT = 8888

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/darshangadkari/Documents/FCA/Library/db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
