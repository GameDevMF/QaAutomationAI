from core.assertions import assert_status


# --- 2. Invalid Endpoint Cases ---
def test_invalid_endpoint(api):
    """Verify that an invalid endpoint returns 404"""

    response, data = api.get("invalid")

    assert_status(response, 404)


# --- 2. ID Edge Cases ---
def test_get_todo_not_found(api):
    """Verify that a non-existent todo ID returns 404"""

    response, data = api.get("/todos/999999")

    assert_status(response, 404)


def test_get_todo_invalid_id_string(api):
    """Verify that an invalid todo ID string returns 404"""

    response, data = api.get("/todos/abc")

    assert_status(response, 404)


def test_get_todo_negative_id(api):
    """Verify that a negative todo ID returns 404"""

    response, data = api.get("/todos/-1")

    assert_status(response, 404)


def test_get_todo_zero_id(api):
    """Verify that a zero todo ID returns 404"""

    response, data = api.get("/todos/0")

    assert_status(response, 404)
