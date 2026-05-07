import os
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from core.api_client import ApiClient

pytest_plugins = ["pytest_playwright"]


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": os.getenv("HEADLESS", "false").lower() == "true",
        "slow_mo": int(os.getenv("SLOW_MO", "500")),
    }


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def api():
    return ApiClient()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
