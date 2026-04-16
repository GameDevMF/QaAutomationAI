import pytest


# --- 1. Happy Path ---
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


@pytest.mark.parametrize("todo_id", [1, 2, 3])
def test_multiple_todos(api, todo_id):
    response = api.get(f"todos/{todo_id}")

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    data = response.json()
    assert data["id"] == todo_id, f"Expected id={todo_id} but got {data['id']}"


# --- 2. Invalid Endpoint Cases ---
def test_invalid_endpoint(api):
    response = api.get("invalid")

    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"


# --- 2. ID Edge Cases ---
def test_get_todo_not_found(api):
    response = api.get("/todos/999999")

    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"


def test_get_todo_invalid_id_string(api):
    response = api.get("/todos/abc")

    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"


def test_get_todo_negative_id(api):
    response = api.get("/todos/-1")

    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"


def test_get_todo_zero_id(api):
    response = api.get("/todos/0")

    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"


# --- 7. Rate Limiting ---
def test_get_todo_rate_limit(api):
    for _ in range(100):  # simulate burst
        response = api.get("/todos/1")

    assert response.status_code in (200, 429), f"Expected status code 200 or 429 but got {response.status_code}"
