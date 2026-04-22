import requests
from core.config import BASE_URL
from core.logger import get_logger

logger = get_logger(__name__)


class ApiClient:
    def get(self, endpoint):
        url = BASE_URL + endpoint
        logger.info(f"GET {url}")

        response = requests.get(url)

        logger.info(f"Response status: {response.status_code}")

        return self._handle_response(response)

    def post(self, endpoint, data):
        url = BASE_URL + endpoint
        logger.info(f"POST {url} | Payload: {data}")

        response = requests.post(url, json=data)

        logger.info(f"Response status: {response.status_code}")

        return self._handle_response(response)

    def _handle_response(self, response):
        try:
            data = response.json()
        except Exception:
            data = None
            logger.warning("Response does not contain valid JSON")

        return response, data
