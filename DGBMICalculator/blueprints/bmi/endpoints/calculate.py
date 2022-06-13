import logging


from flask import request, jsonify

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

try:
    from flask_restplus import Resource
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource

from DGBMICalculator.blueprints.bmi.serializers import bmi_calculation_input
from DGBMICalculator.blueprints.blueprint import api
from DGBMICalculator.blueprints.bmi.formula import bmi_formula
from DGBMICalculator.blueprints.bmi.endpoints.search import BMICategorySearchFloat


log = logging.getLogger(__name__)

ns = api.namespace('bmi/calculate', description='BMI Calculation')

bmi_category_search = BMICategorySearchFloat()


@ns.route('/')
class BMICategoryCollection(Resource):

    @api.response(201, 'BMI successfully calculated.')
    @api.expect([bmi_calculation_input])
    def post(self):
        """
        Creates a new BMI category.
        """
        people = request.json
        logging.debug(f'Input JSON: {people}')

        # count the number of overweight people
        count_overweight = 0

        # loop through to calculate BMI
        for idx, person in enumerate(people):
            bmi = bmi_formula(mass=person['WeightKg'], height=person['HeightCm'])
            bmi_category = bmi_category_search.get(bmi_value=bmi)[0]
            people[idx]['bmi'] = round(bmi,1)
            if bmi_category['bmi_category_name'] == 'Overweight':
                count_overweight += 1
            people[idx]['bmi_category_name'] = bmi_category['bmi_category_name']
            people[idx]['health_risk'] = bmi_category['health_risk']
        logging.debug(f'People: {people}')
        logging.debug(f'Count of Overweight people: {count_overweight}')

        return {'people': people, 'count_overweight': count_overweight}, 201