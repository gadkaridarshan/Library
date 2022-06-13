import pytest
import logging
from DGBMICalculator.app import BMI_SERVER


@pytest.fixture(scope='module')
def client():
    yield BMI_SERVER.app.test_client()

