import pytest


def test_get_todo_by_id(api):
    """Verify that a valid todo ID returns correct data"""

    response = api.get("todos/1")

    expectedText = "Expected status code 200 but got "
    assert response.status_code == 200, f"{expectedText}{response.status_code}"

    data = response.json()

    assert "id" in data, "Response JSON does not contain 'id'"

    expectedText = "Expected id=1 but got "
    assert data["id"] == 1, f"{expectedText}{data['id']}"


def test_get_title(api):
    """Verify that the title of todo ID 1 is correct"""

    response = api.get("todos/1")

    data = response.json()

    expectedText = "Expected title='delectus aut autem' but got "
    title = "delectus aut autem"
    assert data["title"] == title, f"{expectedText}{data['title']}"


@pytest.mark.parametrize("todo_id", [1, 2, 3])
def test_multiple_todos_parametrized(api, todo_id):
    """Verify that multiple todo IDs return correct data parametrization"""

    response = api.get(f"todos/{todo_id}")

    expectedText = "Expected 200 but got "
    assert response.status_code == 200, f"{expectedText}{response.status_code}"

    data = response.json()
    assert data["id"] == todo_id, f"Expected id={todo_id} but got {data['id']}"
