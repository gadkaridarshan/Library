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


bmi_category_add = api.model(
    'BM Category Add/Update',
    {
        'bmi_category_name': fields.String(required=True, description='BMI Category name'),
        'bmi_range_min': fields.Float(required=True, description='BMI Range Min'),
        'bmi_range_max': fields.Float(required=True, description='BMI Range Max'),
        'health_risk': fields.String(required=True, description='Health Risk')
    }
)


bmi_category_search = api.model(
    'BM Category Info',
    {
        'bmi_category_name': fields.String(required=True, description='BMI Category name'),
        'health_risk': fields.String(required=True, description='Health Risk')
    }
)


bmi_calculation_input = api.model(
    'BM Calculation Input',
    {
        'Gender': fields.String(required=False, description='Gender'),
        'HeightCm': fields.Integer(required=False, description='Height in Centimeters'),
        'WeightKg': fields.Integer(required=False, description='Weight in Kilograms')
    }
)

