"""Migrate module for Library."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Library import settings


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = settings.DevelopmentConfig.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initializing migrate.

