import json
from api.client import Client


class Api(Client):
    REGISTRATION = '/register'
    USERS = '/users'
    BASE_URL = 'https://reqres.in/api'

    def list_users(self):
        url = self.BASE_URL + self.USERS + '?page=2'
        return self.get(url)

    def single_user_not_found(self):
        url = self.BASE_URL + self.USERS + '/23'
        return self.get(url)

    def single_user(self):
        url = self.BASE_URL + self.USERS + '/2'
        return self.get(url)

    def create(self, name: str, job: str):
        url = self.BASE_URL + self.USERS
        payload = json.dumps(
            {
                "name": f"{name}",
                "job": f"{job}"
            }
        )
        headers = {'Content-Type': 'application/json'}
        return self.post(url, headers, payload)

    def delete_user(self, id: int):
        url = self.BASE_URL + self.USERS + f'/{id}'
        return self.delete(url)

    def registration(self, email: str, password: str):
        url = self.BASE_URL + self.REGISTRATION
        payload = json.dumps(
            {
                "email": f"{email}",
        	    "password": f"{password}"
            }
        )
        headers = {'Content-Type': 'application/json'}
        return self.post(url, headers, payload)

    def registration_fail(self, email: str):
        url = self.BASE_URL + self.REGISTRATION
        payload = json.dumps(
            {
                "email": f"{email}"
            }
        )
        headers = {'Content-Type': 'application/json'}
        return self.post(url, headers, payload)


api = Api()