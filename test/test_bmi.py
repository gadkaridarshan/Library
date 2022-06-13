import logging
from json import dumps
import pytest
from sqlalchemy.orm.exc import NoResultFound


def test_get_bmi_categories(client):
    # test call to bmi/categories/
    response = client.get("/api/bmi/categories/")

    # Validate
    assert response.status_code == 200
    assert type(response.json) == list
    assert len(response.json) > 0


def test_get_bmi_category_post(client):
    content_type = 'application/json'
    headers = {
        'Content-Type': content_type,
        'Accept': content_type
    }
    data = {
        "bmi_category_name": "V Severely Obese",
        "bmi_range_min": 350,
        "bmi_range_max": 399.9,
        "health_risk": "V High Risk"
    }
    # test call to bmi/categories/
    response = client.post("/api/bmi/categories/", data=dumps(data), headers=headers)

    # Validate
    assert response.status_code == 201
    assert response.content_type == content_type
    assert response.json is None


@pytest.mark.parametrize("test_id", range(7, 8))
def test_get_bmi_category_pass(client, test_id):
    logging.info(f'id: {test_id}')
    # first find out if that record exists
    response = client.get(f"/api/bmi/categories/{test_id}")
    logging.info(f'response status code: {response.status_code}')

    content_type = 'application/json'

    assert response.status_code == 200
    assert response.content_type == content_type


@pytest.mark.parametrize("test_id", range(8, 9))
def test_get_bmi_category_fail(client, test_id):
    logging.info(f'id: {test_id}')
    # first find out if that record exists
    response = client.get(f"/api/bmi/categories/{test_id}")
    logging.info(f'response status code: {response.status_code}')

    content_type = 'application/json'

    assert response.status_code == 404
    assert response.content_type == content_type


def check_if_bmi_category_exists_success(client, test_id):
    logging.info(f'id: {test_id}')
    # first find out if that record exists
    response = client.get(f"/api/bmi/categories/{test_id}")
    logging.info(f'response status code: {response.status_code}')
    return response.status_code


@pytest.mark.parametrize("test_id", range(7, 8))
def test_get_bmi_category_delete_pass(client, test_id):
    if check_if_bmi_category_exists_success(client=client,test_id=test_id) == 200:
        logging.info(f'Record with id: {test_id} is in the system and hence ' + \
                     'the associated record can be deleted')

        content_type = 'application/json'
        headers = {
            'Content-Type': content_type,
            'Accept': content_type
        }

        try:
            # test call to bmi/categories/
            response = client.delete(f"/api/bmi/categories/{test_id}", headers=headers)

            # Validate
            assert response.status_code in (204, 404)
            assert response.content_type == content_type
        except NoResultFound as nrf:
            logging.info(f'NoResultFound exception is thrown. Record with id: {test_id} ' + \
                         'is not in the system so the associated record cannot be deleted')


@pytest.mark.parametrize("test_id", range(8, 9))
def test_get_bmi_category_delete_fail(client, test_id):
    if check_if_bmi_category_exists_success(client=client,test_id=test_id) == 404:
        logging.info(f'NoResultFound exception is thrown. Record with id: {test_id} ' + \
                     'is not in the system so the associated record cannot be deleted')


@pytest.mark.parametrize("test_id", range(5, 6))
def test_get_bmi_category_put_pass(client, test_id):
    if check_if_bmi_category_exists_success(client=client, test_id=test_id) == 200:
        logging.info(f'Record with id: {test_id} is in the system and hence ' + \
                     'the associated record can be updated')

        content_type = 'application/json'
        headers = {
            'Content-Type': content_type,
            'Accept': content_type
        }

        # update bmi_range_max
        data = {
            "bmi_category_name": "Severely Obese",
            "bmi_range_min": 35,
            "bmi_range_max": 40.9,
            "health_risk": "High Risk"
        }
        # test call to bmi/categories/
        response = client.put(f"/api/bmi/categories/{test_id}", data=dumps(data), headers=headers)

        # Validate
        assert response.status_code == 204
        assert response.content_type == content_type

        # update bmi_range_max to the old correct value
        data = {
            "bmi_category_name": "Severely Obese",
            "bmi_range_min": 35,
            "bmi_range_max": 39.9,
            "health_risk": "High Risk"
        }
        # test call to bmi/categories/
        response = client.put(f"/api/bmi/categories/{test_id}", data=dumps(data), headers=headers)

        # Validate
        assert response.status_code == 204
        assert response.content_type == content_type


@pytest.mark.parametrize("test_id", range(8, 9))
def test_get_bmi_category_update_fail(client, test_id):
    if check_if_bmi_category_exists_success(client=client,test_id=test_id) == 404:
        logging.info(f'NoResultFound exception is thrown. Record with id: {test_id} ' + \
                     'is not in the system so the associated record cannot be updated')

