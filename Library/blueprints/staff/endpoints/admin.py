"""Staff Admin module."""
import logging

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Resource
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource


from Library.blueprints.staff.actions import (
    update_book_availability_status_to_available,
    update_book_availability_status_to_borrowed,
    get_rented_report,
    load_books_data,
    populate_amazon_url_id
)

from Library.blueprints.staff.serializers import book_search
from Library.blueprints.blueprint import api


log = logging.getLogger(__name__)

ns = api.namespace('staff/admin', description='Staff admin namespace')


@ns.route('/update_availability_to_available/<int:book_id>')
class UpdateBookAvailabilityStatusToAvailable(Resource):
    """Class to update status to Available."""

    @api.response(201, 'Book availability updated to Available.')
    def put(self, book_id):
        """Update book availability status to Availability."""
        return update_book_availability_status_to_available(book_id=book_id)


@ns.route('/update_availability_to_borrowed/<int:book_id>')
class UpdateBookAvailabilityStatusToBorrowed(Resource):
    """Class to update status to Borrowed."""

    @api.response(201, 'Book availability updated to Borrowed.')
    def put(self, book_id):
        """Update book availability status to Borrowed."""
        return update_book_availability_status_to_borrowed(book_id=book_id)


@ns.route('/generate_report')
class GenerateReport(Resource):
    """Class to Generate Report."""

    @api.response(201, 'Report of rented/borrowed books.')
    @api.marshal_with(book_search)
    def get(self):
        """Generate report of rented/borrowed books."""
        return get_rented_report()


@ns.route('/load_books_data')
class LoadBooksData(Resource):
    """Class to Load Books Data."""

    @api.response(201, 'Books Data Loaded.')
    def get(self):
        """Load books data from the provided csv."""
        return load_books_data()


@ns.route('/populate_amazon_url_id')
class PopulateAmazonUrlId(Resource):
    """Class to populate Amazon URL Id."""

    @api.response(201, 'Amazon URLs and Ids generated and populated in the Books table.')
    def get(self):
        """Generate and populate in the Books table."""
        return populate_amazon_url_id()

