import pytest
from core.assertions import assert_status, assert_data


def test_get_todo_by_id(api):
    """Verify that a valid todo ID returns correct data"""

    response, data = api.get("todos/1")

    assert_status(response, 200)

    assert_data(data, "id", 1)


def test_get_title(api):
    """Verify that the title of todo ID 1 is correct"""

    response, data = api.get("todos/1")

    assert_status(response, 200)

    assert_data(data, "title", "delectus aut autem")


@pytest.mark.parametrize("todo_id", [1, 2, 3])
def test_multiple_todos_parametrized(api, todo_id):
    """Verify that multiple todo IDs return correct data parametrization"""

    response, data = api.get(f"todos/{todo_id}")

    assert_status(response, 200)

    assert_data(data, "id", todo_id)
