from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def navigate(self):
        super().navigate("https://www.saucedemo.com/")

    def login(self, user):
        self.page.fill(self.username_input, user["username"])
        self.page.fill(self.password_input, user["password"])
        self.page.click(self.login_button)

        return InventoryPage(self.page)

    def is_logged_in(self):
        return self.page.locator(".inventory_list").is_visible()
