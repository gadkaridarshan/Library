"""Users Serializers module."""
from flask_restplus import fields


from Library.blueprints.blueprint import api


book_search = api.model(
    'Book Info',
    {
        'book_id': fields.Integer(required=True, description='Book Id'),
        'book_ISBN': fields.String(required=True, description='Book ISBN'),
        'book_authors': fields.String(required=True, description='Book Authors'),
        'book_publication_year': fields.Integer(required=True, description='Book Publication Year'),
        'book_title': fields.String(required=True, description='Book Title'),
        'book_language': fields.String(required=True, description='Book Language'),
        'book_availability': fields.String(required=True, description='Book Availability', default=True)
    }
)


wish = api.model(
    'Wish Add/Delete/List',
    {
        'book_id': fields.Integer(required=True, description='Book Id'),
        'user_id': fields.Integer(required=True, description='User Id'),
        'created_at': fields.DateTime(required=False, description='Wish Entry Creation Time')
    }
)

