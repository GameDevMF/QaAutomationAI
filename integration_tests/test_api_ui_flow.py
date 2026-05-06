import pytest

from flows.api_ui_flows import create_post_and_login
from test_data.todo_data import POST_PAYLOAD
from test_data.user_data import VALID_USER


@pytest.mark.integration
@pytest.mark.parametrize("payload", [
    POST_PAYLOAD,
    {"title": "another", "body": "test", "userId": 2}
])
@pytest.mark.parametrize("user", [VALID_USER])
def test_create_post_and_login(api, login_page, inventory_page, user, payload):
    create_post_and_login(
        api,
        login_page,
        inventory_page,
        user,
        payload
    )
