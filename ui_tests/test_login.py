import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_login_success(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 1. Navigate to the login page
    login_page.navigate()

    # 2. Perform login with valid credentials
    login_page.login("standard_user", "secret_sauce")

    # 3. Assertions: Verify the user is logged in by
    # checking for a specific element on the landing page
    assert login_page.is_logged_in(), \
        "Login was not successful, inventory list is not visible"

    # 4. Assertions: Verify the URL and success message
    # Expect the URL to change to the logged-in landing page
    assert page.url == "https://www.saucedemo.com/inventory.html", \
        "URL did not change to inventory page after login"

    # 5. Assertions: Check for a specific success element on the page
    assert inventory_page.is_loaded().is_visible(), \
        "Inventory page is not loaded after login"
