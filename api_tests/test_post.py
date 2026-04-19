from core.assertions import assert_status, assert_data


def test_post_request(api, post_payload):
    """Verify that a POST request creates a new resource with correct data"""

    response, data = api.post("posts", post_payload)

    assert_status(response, 201)

    assert_data(data, "title", post_payload['title'])
    assert_data(data, "body", post_payload['body'])
    assert_data(data, "userId", post_payload['userId'])
