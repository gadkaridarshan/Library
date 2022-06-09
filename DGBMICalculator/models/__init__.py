from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database():
    from DGBMICalculator.models.models import BMI  # noqa
    db.drop_all()
    db.create_all()