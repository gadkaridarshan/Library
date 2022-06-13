import pytest


@pytest.mark.parametrize("test_bmi_value", range(1, 16))
def test_get_bmi_category_underweight(client, test_bmi_value):
    # test call to bmi/categories/
    response = client.get(f"/api/bmi/categories_search/{test_bmi_value/2}")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == dict
    assert response.json['bmi_category_name'] == "Underweight"
    assert response.json['health_risk'] == "Malnutrition Risk"


@pytest.mark.parametrize("test_bmi_value", range(185, 249))
def test_get_bmi_category_normal_weight(client, test_bmi_value):
    # test call to bmi/categories/
    response = client.get(f"/api/bmi/categories_search/{test_bmi_value/10}")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == dict
    assert response.json['bmi_category_name'] == "Normal Weight"
    assert response.json['health_risk'] == "Low Risk"


@pytest.mark.parametrize("test_bmi_value", range(250, 299))
def test_get_bmi_category_overweight(client, test_bmi_value):
    # test call to bmi/categories/
    response = client.get(f"/api/bmi/categories_search/{test_bmi_value/10}")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == dict
    assert response.json['bmi_category_name'] == "Overweight"
    assert response.json['health_risk'] == "Enhanced Risk"


@pytest.mark.parametrize("test_bmi_value", range(300, 349))
def test_get_bmi_category_moderately_obese(client, test_bmi_value):
    # test call to bmi/categories/
    response = client.get(f"/api/bmi/categories_search/{test_bmi_value/10}")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == dict
    assert response.json['bmi_category_name'] == "Moderately Obese"
    assert response.json['health_risk'] == "Medium Risk"


@pytest.mark.parametrize("test_bmi_value", range(350, 399))
def test_get_bmi_category_severely_obese(client, test_bmi_value):
    # test call to bmi/categories/
    response = client.get(f"/api/bmi/categories_search/{test_bmi_value/10}")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == dict
    assert response.json['bmi_category_name'] == "Severely Obese"
    assert response.json['health_risk'] == "High Risk"


@pytest.mark.parametrize("test_bmi_value", range(400, 499))
def test_get_bmi_category_very_severely_obese(client, test_bmi_value):
    # test call to bmi/categories/
    response = client.get(f"/api/bmi/categories_search/{test_bmi_value/10}")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == dict
    assert response.json['bmi_category_name'] == "Very Severely Obese"
    assert response.json['health_risk'] == "Very High Risk"

