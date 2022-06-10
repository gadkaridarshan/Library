import logging


from sqlalchemy.orm import load_only


import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Resource
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource

from DGBMICalculator.blueprints.bmi.serializers import bmi_category_search
from DGBMICalculator.blueprints.blueprint import api
from DGBMICalculator.models.models import BMI


log = logging.getLogger(__name__)

ns = api.namespace('bmi/categories_search', description='Search related to BMI categories')


def calculate_bmi(bmi_value):
    bmi_value = round(bmi_value, 1)
    return_fields = ['bmi_category_name', 'health_risk']
    return BMI.query.filter(
        bmi_value >= BMI.bmi_range_min,
        bmi_value <= BMI.bmi_range_max
    ).options(load_only(*return_fields)).one(), 200


@ns.route('/<float:bmi_value>')
@api.response(404, 'BMI Category not found.')
class BMICategorySearchInt(Resource):

    @api.marshal_with(bmi_category_search)
    def get(self, bmi_value):
        """
        Returns a specific BMI category.
        """
        # round bmi_value to one digit after the decimal point
        logging.debug(f'BMI Value: {bmi_value}')
        return calculate_bmi(bmi_value=bmi_value)


@ns.route('/<int:bmi_value>')
@api.response(404, 'BMI Category not found.')
class BMICategorySearchFloat(Resource):

    @api.marshal_with(bmi_category_search)
    def get(self, bmi_value):
        """
        Returns a specific BMI category.
        """
        # round bmi_value to one digit after the decimal point
        logging.debug(f'BMI Value: {bmi_value}')
        bmi_value = float(bmi_value)
        return calculate_bmi(bmi_value=bmi_value)

