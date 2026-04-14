import requests


def test_get_todo():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    data = response.json()

    assert data["id"] == 1, f"Expected id=1 but got {data['id']}"


def test_get_title():
    import requests

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    data = response.json()

    assert data["title"] == "delectus aut autem", f"Expected title='delectus aut autem' but got {data['title']}"


def test_post_request():
    import requests

    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

    data = response.json()
    assert data["title"] == "foo", f"Expected title='foo' but got {data['title']}"


def test_invalid_endpoint():
    response = requests.get("https://jsonplaceholder.typicode.com/invalid")

    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
