"""Models module."""
from datetime import datetime

from Library.models import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


class Book(db.Model):
    """Class for Book model."""

    __tablename__ = 'Book'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer)
    book_ISBN = db.Column(db.String(20))
    book_authors = db.Column(db.String(100))
    book_publication_year = db.Column(db.Integer)
    book_title = db.Column(db.String(100))
    book_language = db.Column(db.String(50))
    book_availability = db.Column(db.String(5))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    rented_at = db.Column(db.DateTime)

    def __init__(
            self,
            book_id,
            book_ISBN,
            book_authors,
            book_publication_year,
            book_title,
            book_language,
            book_availability
    ):
        """Construct."""
        self.book_id = book_id
        self.book_ISBN = book_ISBN
        self.book_authors = book_authors
        self.book_publication_year = book_publication_year
        self.book_title = book_title
        self.book_language = book_language
        self.book_availability = book_availability

    def __repr__(self):
        """Representation method."""
        return '<Book: %r>' % self.book_title


class User(db.Model):
    """Class for User model."""

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    def __init__(self, first_name, last_name):
        """Construct."""
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        """Representation method."""
        return '<User ID: %r, First Name: %r, Last Name: %r>' % (self.id, self.first_name, self.last_name)


class Wish(db.Model):
    """Class for User Wish / Wishlist model."""

    __tablename__ = 'Wish'

    book_id = db.Column(db.Integer, ForeignKey('Book.book_id'), primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('User.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    book = relationship("Book", backref=backref("Wish", uselist=False))
    user = relationship("User", backref=backref("Wish", uselist=False))

    def __init__(self, book_id, user_id):
        """Construct."""
        self.book_id = book_id
        self.user_id = user_id

    def __repr__(self):
        """Representation method."""
        return '<Book ID: %r, User ID: %r>' % (self.book_id, self.user_id)
