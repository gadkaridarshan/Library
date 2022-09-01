"""Staff Serializers module."""
from flask_restplus import fields


from Library.blueprints.blueprint import api


all_users = api.model(
    'All Users Info',
    {
        'id': fields.Integer(required=True, description='Id'),
        'first_name': fields.String(required=True, description='First Name'),
        'last_name': fields.String(required=True, description='Last Name')
    }
)


all_wishes = api.model(
    'All Wishlists Info',
    {
        'book_id': fields.Integer(required=True, description='Book Id'),
        'user_id': fields.Integer(required=True, description='User Id'),
        'created_at': fields.DateTime(required=False, description='Wish Entry Creation Time')
    }
)


book_search = api.model(
    'Book Info',
    {
        'book_id': fields.Integer(required=True, description='Book Id'),
        'book_ISBN': fields.String(required=True, description='Book ISBN'),
        'book_authors': fields.String(required=True, description='Book Authors'),
        'book_publication_year': fields.Integer(required=True, description='Book Publication Year'),
        'book_title': fields.String(required=True, description='Book Title'),
        'book_language': fields.String(required=True, description='Book Language'),
        'book_availability': fields.String(required=True, description='Book Availability', default=True),
        'created_at': fields.DateTime(required=False, description='Wish Entry Creation Time'),
        'rented_at': fields.DateTime(required=False, description='Wish Entry Creation Time'),
        'rented_for_in_days': fields.Integer(description='Rented for, in days'),
        'rented_for_in_seconds': fields.Integer(description='Rented for, in seconds')
    }
)

