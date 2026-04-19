import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,  # This forces the browser to pop up
        "slow_mo": 500,     # Optional: adds a delay so you can actually see it
    }
