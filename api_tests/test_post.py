def test_post_request(api, post_payload):
    """Verify that a POST request creates a new resource with correct data"""

    response = api.post("posts", post_payload)

    expectedText = "Expected status code 201 but got "
    assert response.status_code == 201, f"{expectedText}{response.status_code}"

    data = response.json()

    expectedText = f"Expected title='{post_payload['title']}' "
    expectedText += f"but got {data['title']}"
    assert data["title"] == post_payload["title"], expectedText

    expectedText = f"Expected body='{post_payload['body']}' "
    expectedText += f"but got {data['body']}"
    assert data["body"] == post_payload["body"], expectedText

    expectedText = f"Expected userId='{post_payload['userId']}' "
    expectedText += f"but got {data['userId']}"
    assert data["userId"] == post_payload["userId"], expectedText
