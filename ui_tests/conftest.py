import os
import pytest
from playwright.sync_api import sync_playwright


def is_headless():
    return os.getenv("HEADLESS", "false").lower() == "true"


def get_slow_mo():
    return int(os.getenv("SLOW_MO", "500"))


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=is_headless(),
            slow_mo=get_slow_mo()
        )
        page = browser.new_page()
        yield page
        browser.close()
