from flask_restplus import fields
from DGBMICalculator.blueprints.blueprint import api

bmi_category = api.model(
    'BM Category',
    {
        'id': fields.Integer(readOnly=True, description='The unique identifier of a bmi category'),
        'bmi_category_name': fields.String(required=True, description='BMI Category name'),
        'bmi_range_min': fields.Float(required=True, description='BMI Range Min'),
        'bmi_range_max': fields.Float(required=True, description='BMI Range Max'),
        'health_risk': fields.String(required=True, description='Health Risk')
    }
)