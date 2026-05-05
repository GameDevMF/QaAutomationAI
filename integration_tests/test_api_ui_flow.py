import pytest

from core.assertions import assert_status
from test_data.todo_data import POST_PAYLOAD
from test_data.user_data import VALID_USER


@pytest.mark.integration
def test_create_post_and_login(api, login_page, inventory_page):
    # Step 1: Create data via API
    response, data = api.post("posts", POST_PAYLOAD)

    assert_status(response, 201)

    login_page.navigate()
    login_page.login(VALID_USER)

    # Step 3: Validate UI loaded
    assert inventory_page.is_loaded()
