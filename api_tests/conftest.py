import pytest
from core.api_client import ApiClient


@pytest.fixture
def api():
    return ApiClient()
