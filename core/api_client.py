import requests
from core.config import BASE_URL


class ApiClient:
    def get(self, endpoint):
        response = requests.get(BASE_URL + endpoint)
        return self._handle_response(response)

    def post(self, endpoint, data):
        response = requests.post(BASE_URL + endpoint, json=data)
        return self._handle_response(response)

    def _handle_response(self, response):
        try:
            data = response.json()
        except Exception:
            data = None

        return response, data
