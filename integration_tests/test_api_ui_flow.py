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
def test_create_post_and_login(env, api, login_page, inventory_page, user, payload):
    print(f"Running against environment: {env}")

    assert env in ["dev", "staging", "prod"]

    title, _ = create_post_and_login(
        api,
        login_page,
        inventory_page,
        user,
        payload
    )

    count = inventory_page.get_inventory_count()

    assert count > 0, "Inventory count should be greater than 0"
    assert isinstance(title, str), "Title should be a non-empty string"


@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    pass


@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert False
