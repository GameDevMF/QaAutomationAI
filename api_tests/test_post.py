from core.assertions import assert_status, assert_data
from test_data.todo_data import POST_PAYLOAD


def test_post_request(api):
    """Verify that a POST request creates a new resource with correct data"""

    response, data = api.post("posts", POST_PAYLOAD)

    assert_status(response, 201)

    assert_data(data, "title", POST_PAYLOAD['title'])
    assert_data(data, "body", POST_PAYLOAD['body'])
    assert_data(data, "userId", POST_PAYLOAD['userId'])
