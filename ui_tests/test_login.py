import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_login_success(page: Page):
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
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Check for a specific success element on the page
    success_message = page.locator(".inventory_list")
    expect(success_message).to_be_visible()
