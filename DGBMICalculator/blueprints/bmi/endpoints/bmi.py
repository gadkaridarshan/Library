import logging


from flask import request

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Resource
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource


from DGBMICalculator.blueprints.bmi.actions import create_bmi_category, update_bmi_category, delete_bmi_category
from DGBMICalculator.blueprints.bmi.serializers import bmi_category
from DGBMICalculator.blueprints.blueprint import api
from DGBMICalculator.models.models import BMI


log = logging.getLogger(__name__)

ns = api.namespace('bmi/categories', description='Operations related to BMI categories')


@ns.route('/')
class BMICategoryCollection(Resource):

    @api.marshal_list_with(bmi_category)
    def get(self):
        """
        Returns list of BMI categories.
        """
        logging.info(f'All BMI Categories requested')
        bmis = BMI.query.all()
        return bmis, 200

    @api.response(201, 'BMI successfully created.')
    @api.expect(bmi_category)
    def post(self):
        """
        Creates a new BMI category.
        """
        data = request.json
        create_bmi_category(data=data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'BMI Category not found.')
class BMICategoryItem(Resource):

    @api.marshal_with(bmi_category)
    def get(self, id):
        """
        Returns a specific BMI category.
        """
        return BMI.query.filter(BMI.id == id).one()

    @api.expect(bmi_category)
    @api.response(204, 'BMI Category successfully updated.')
    def put(self, id):
        """
        Updates a BMI category.
        Use this method to change the name of a BMI category.
        * Send a JSON object with the new name in the request body.
        ```
        {
          "bmi_category_name": "New Category Name",
          "bmi_range_min": "BMI Category Range Min Value",
          "bmi_range_max": "BMI Category Range Max Value",
          "health_risk": "Health Risk"
        }
        ```
        * Specify the ID of the BMI category to modify in the request URL path.
        """
        data = request.json
        update_bmi_category(bmi_category_id=id, data=data)
        return None, 204

    @api.response(204, 'BMI Category successfully deleted.')
    def delete(self, id):
        """
        Deletes BMI category.
        """
        delete_bmi_category(bmi_category_id=id)
        return None, 204

