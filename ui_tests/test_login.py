import pytest


@pytest.mark.ui
def test_login_success(page):

    # 1. Navigate to the login page
    page.goto("https://www.saucedemo.com/")

    # 2. Fill in the credentials
    # Using CSS selectors for username and password fields
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    # 3. Click the submit button
    page.click("#login-button")

    # 4. Assertions: Verify the URL and success message
    # Expect the URL to change to the logged-in landing page
    assert page.url == "https://www.saucedemo.com/inventory.html", \
        "URL did not change to inventory page after login"

    # Check for a specific success element on the page
    success_message = page.locator(".inventory_list")
    assert success_message.is_visible(), \
        "Success message is not visible after login"
