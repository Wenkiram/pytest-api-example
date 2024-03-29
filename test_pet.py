from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

# Test to validate the schema of a pet
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
        try:
             validate(instance=response.json(), schema=schemas.pet)
        except Exception as e:
            pytest.fail(f"Response schema validation failed: {str(e)}")

@pytest.mark.parametrize("status", ["available", "sold", "pending"])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)

    assert response.status_code == 200

    # Validate the 'status' property in the response is equal to the expected status
    for pet in response.json():
        assert pet['status'] == status

    # Validate the schema for each object in the response
    try:
        for pet in response.json():
            validate(instance=pet, schema=schemas.pet)
    except Exception as e:
        pytest.fail(f"Response schema validation failed: {str(e)}")

def test_get_by_id_404():
    # Testing and validating the appropriate 404 response for /pets/{pet_id}
    test_endpoint = "/pets/1000"  # Assuming this ID doesn't exist

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 404
    pass
