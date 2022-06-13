from json import dumps


def test_calculate_pass(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
            { "Gender": "Male", "HeightCm": 161, "WeightKg": 85},
            { "Gender": "Male", "HeightCm": 180, "WeightKg": 77},
            { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    # test call to bmi/categories/
    response = client.post("/api/bmi/calculate/", data=dumps(data), headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json['people'] == [
        {'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96,
         'bmi': 32.8, 'bmi_category_name': 'Moderately Obese', 'health_risk': 'Medium Risk'},
        {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85,
         'bmi': 32.8, 'bmi_category_name': 'Moderately Obese', 'health_risk': 'Medium Risk'},
        {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77,
         'bmi': 23.8, 'bmi_category_name': 'Normal Weight', 'health_risk': 'Low Risk'},
        {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62,
         'bmi': 22.5, 'bmi_category_name': 'Normal Weight', 'health_risk': 'Low Risk'},
        {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70,
         'bmi': 31.1, 'bmi_category_name': 'Moderately Obese', 'health_risk': 'Medium Risk'},
        {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82,
         'bmi': 29.4, 'bmi_category_name': 'Overweight', 'health_risk': 'Enhanced Risk'}
    ]
    assert  response.json['count_overweight'] == 1


def test_calculate_pass(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
            { "Gender": "Male", "HeightCm": 161, "WeightKg": 85},
            { "Gender": "Male", "HeightCm": 180},
            { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    # test call to bmi/categories/
    response = client.post("/api/bmi/calculate/", data=dumps(data), headers=headers)

    # Validate
    assert response.status_code == 500
    assert response.content_type == content_type

