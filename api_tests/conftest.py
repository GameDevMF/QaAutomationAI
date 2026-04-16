import pytest
from core.api_client import ApiClient


@pytest.fixture
def api():
    return ApiClient()


@pytest.fixture
def post_payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }