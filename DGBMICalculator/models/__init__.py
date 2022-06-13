"""init module for models"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    """Function to reset the database"""
    db.drop_all()
    db.create_all()
