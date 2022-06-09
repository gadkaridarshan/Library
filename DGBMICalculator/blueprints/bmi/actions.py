from DGBMICalculator.models import db
from DGBMICalculator.models.models import BMI


def create_bmi_category(data):

    bmi = BMI(
        bmi_category_name=data.get('bmi_category_name'),
        bmi_range_min=data.get('bmi_range_min'),
        bmi_range_max=data.get('bmi_range_max'),
        health_risk=data.get('health_risk')
    )

    db.session.add(bmi)
    db.session.commit()


def update_bmi_category(bmi_category_id, data):

    bmi = BMI.query.filter(BMI.id == bmi_category_id).one()

    bmi.bmi_category_name = data.get('bmi_category_name')
    bmi.bmi_range_min = data.get('bmi_range_min')
    bmi.bmi_range_max = data.get('bmi_range_max')
    bmi.health_risk = data.get('health_risk')

    db.session.add(bmi)
    db.session.commit()


def delete_bmi_category(bmi_category_id):

    bmi = BMI.query.filter(BMI.id == bmi_category_id).one()

    db.session.delete(bmi)
    db.session.commit()


