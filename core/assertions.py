def assert_status(response, expected_status):
    assert response.status_code == expected_status, \
        f"Expected status {expected_status} but got {response.status_code}"


def assert_data(data, parameter, expected_value):
    assert data is not None, "Response JSON is None"

    assert parameter in data, f"Response JSON does not contain '{parameter}'"

    assert data[parameter] == expected_value, \
        f"Expected '{parameter}'={expected_value} but got {data[parameter]}"
