from core.assertions import assert_status


def create_post_and_login(api, login_page, inventory_page, user, payload):
    # Step 1: API call
    response, data = api.post("posts", payload)

    assert_status(response, 201)
    assert data is not None

    assert "id" in data
    assert isinstance(data["id"], int)

    # Step 2: UI login
    login_page.navigate()
    login_page.login(user)

    assert inventory_page.is_loaded()

    return {
        "title": payload.get("title"),
        "id": data.get("id")
    }
