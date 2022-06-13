"""Models module"""
from DGBMICalculator.models import db


class BMI(db.Model):
    """Class for BMI model"""

    __tablename__ = 'BMI'

    id = db.Column(db.Integer, primary_key=True)
    bmi_category_name = db.Column(db.String(50))
    bmi_range_min = db.Column(db.Float)
    bmi_range_max = db.Column(db.Float)
    health_risk = db.Column(db.String(50))

    def __init__(self, bmi_category_name, bmi_range_min, bmi_range_max, health_risk):
        """Constructor"""
        self.bmi_category_name = bmi_category_name
        self.bmi_range_min = bmi_range_min
        self.bmi_range_max = bmi_range_max
        self.health_risk = health_risk

    def __repr__(self):
        """Representation method"""
        return '<BMI Category %r>' % self.bmi_category
