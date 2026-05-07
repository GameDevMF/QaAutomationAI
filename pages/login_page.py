from core.config import UI_BASE_URL
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username_input_selector = "#user-name"
        self.password_input_selector = "#password"
        self.login_button_selector = "#login-button"

    def navigate(self):
        super().navigate(UI_BASE_URL)

    def login(self, user):
        self.page.fill(self.username_input_selector, user["username"])
        self.page.fill(self.password_input_selector, user["password"])
        self.page.click(self.login_button_selector)
        self.page.wait_for_load_state("networkidle")

        return InventoryPage(self.page)

    def is_logged_in(self):
        return self.page.locator(".inventory_list").is_visible()
