from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

def test_patch_order_by_id():
    # Create a new order to patch
    new_order = {'pet_id': 0}  # Assuming pet with ID 0 is available

    # Place a new order
    place_order_response = api_helpers.post_api_data('/store/order', new_order)
    assert place_order_response.status_code == 201

    # Extract the order ID from the response
    order_id = place_order_response.json()['id']

    # Prepare data for patching the order
    update_data = {'status': 'sold'}

    # Patch the order
    patch_order_response = api_helpers.patch_api_data(f'/store/order/{order_id}', update_data)

    # Validate the response code
    assert patch_order_response.status_code == 200

    # Validate the response message
    assert patch_order_response.json()["message"] == "Order and pet status updated successfully"
    pass
