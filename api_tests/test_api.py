def test_get_todo(api):
    response = api.get("todos/1")

    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    data = response.json()

    assert "id" in data, "Response JSON does not contain 'id'"

    assert data["id"] == 1, f"Expected id=1 but got {data['id']}"


def test_get_title(api):
    response = api.get("todos/1")

    data = response.json()

    assert data["title"] == "delectus aut autem", f"Expected title='delectus aut autem' but got {data['title']}"


def test_post_request(api, post_payload):
    response = api.post("posts", post_payload)

    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

    data = response.json()
    assert data["title"] == post_payload["title"], f"Expected title='{post_payload['title']}' but got {data['title']}"
    assert data["body"] == post_payload["body"], f"Expected body='{post_payload['body']}' but got {data['body']}"
    assert data["userId"] == post_payload["userId"], f"Expected userId='{post_payload['userId']}' but got {data['userId']}"


def test_invalid_endpoint(api):
    response = api.get("invalid")

    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
