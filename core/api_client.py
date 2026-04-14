import requests


class ApiClient:
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    def get(self, endpoint):
        return requests.get(self.BASE_URL + endpoint)

    def post(self, endpoint, data):
        return requests.post(self.BASE_URL + endpoint, json=data)
