import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.user_data import VALID_USER, INVALID_USER


@pytest.mark.ui
def test_login_success(page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    inventory_page = login_page.login(VALID_USER)

    assert inventory_page.is_loaded(), \
        "Login was not successful, inventory list is not visible"


@pytest.mark.ui
@pytest.mark.negative
def test_login_invalid_user(page):
    login_page = LoginPage(page)

    login_page.navigate()
    inventory_page = login_page.login(INVALID_USER)

    assert not inventory_page.is_loaded(), "Login should have failed but succeeded"

    # Optionally, check for an error message
    error_message = page.locator(".error-message-container").text_content()
    assert error_message is not None and "Username and password do not match" in error_message, \
        f"Expected error message not found, got: {error_message}"
