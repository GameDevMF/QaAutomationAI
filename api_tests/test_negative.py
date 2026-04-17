expectedText = "Expected status code 404 but got "


# --- 2. Invalid Endpoint Cases ---
def test_invalid_endpoint(api):
    """Verify that an invalid endpoint returns 404"""

    response = api.get("invalid")

    assert response.status_code == 404, f"{expectedText}{response.status_code}"


# --- 2. ID Edge Cases ---
def test_get_todo_not_found(api):
    """Verify that a non-existent todo ID returns 404"""

    response = api.get("/todos/999999")

    assert response.status_code == 404, f"{expectedText}{response.status_code}"


def test_get_todo_invalid_id_string(api):
    """Verify that an invalid todo ID string returns 404"""

    response = api.get("/todos/abc")

    assert response.status_code == 404, f"{expectedText}{response.status_code}"


def test_get_todo_negative_id(api):
    """Verify that a negative todo ID returns 404"""

    response = api.get("/todos/-1")

    assert response.status_code == 404, f"{expectedText}{response.status_code}"


def test_get_todo_zero_id(api):
    """Verify that a zero todo ID returns 404"""

    response = api.get("/todos/0")

    assert response.status_code == 404, f"{expectedText}{response.status_code}"


# --- 7. Rate Limiting ---
def test_get_todo_rate_limit(api):
    """Verify that many requests in a short time may trigger rate limiting"""

    for _ in range(100):  # simulate burst
        response = api.get("/todos/1")

    expectedText = "Expected status code 200 or 429 but got "
    expectedText += f"{response.status_code}"

    assert response.status_code in (200, 429), f"{expectedText}"
