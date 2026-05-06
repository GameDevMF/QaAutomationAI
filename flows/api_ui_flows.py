from core.assertions import assert_status


def create_post_and_login(api, login_page, inventory_page, user, payload):
    # API step
    response, _ = api.post("posts", payload)

    assert_status(response, 201)

    # UI step
    login_page.navigate()
    login_page.login(user)

    assert inventory_page.is_loaded()
