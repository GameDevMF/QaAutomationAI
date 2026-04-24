import pytest
from core.assertions import assert_status, assert_data
from test_data.todo_data import VALID_TODO
from test_data.todo_data import MULTIPLE_TODOS
from core.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.api
@pytest.mark.smoke
def test_get_todo_by_id(api):
    logger.info("Starting test: test_get_todo_by_id")
    """Verify that a valid todo ID returns correct data"""

    response, data = api.get("todos/1")

    assert_status(response, 200)

    assert_data(data, "id", VALID_TODO["id"])


@pytest.mark.api
def test_get_title(api):
    """Verify that the title of todo ID 1 is correct"""

    response, data = api.get("todos/1")

    assert_status(response, 200)

    assert_data(data, "title", VALID_TODO["title"])


@pytest.mark.api
@pytest.mark.parametrize("todo_id", MULTIPLE_TODOS)
def test_multiple_todos_parametrized(api, todo_id):
    """Verify that multiple todo IDs return correct data parametrization"""

    response, data = api.get(f"todos/{todo_id}")

    assert_status(response, 200)

    assert_data(data, "id", todo_id)
