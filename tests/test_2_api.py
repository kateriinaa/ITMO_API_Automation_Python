from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert
import re


def test_list_users():
    res = api.list_users()
    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json())
    assert res.headers['Cache-Control'] == 'max-age=14400'


def test_single_user_not_found():
    res = api.single_user_not_found()
    assert res.status_code == HTTPStatus.NOT_FOUND


def test_single_user():
    res = api.single_user()
    res_body = res.json()
    assert res.status_code == HTTPStatus.OK
    assert res_body['data']['first_name'] == 'Janet'
    assert re.fullmatch(r'\w+', res_body['data']['last_name'])
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }

    assert res_body == example


def test_create():
    name = "Alex"
    job = "QA"
    res = api.create(name, job)

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()["name"] == name
    assert res.json()["job"] == job
    id = res.json()["id"]
    assert re.fullmatch(r'\d{1,4}', id)
    res_delete = api.delete_user(id)
    assert res_delete.status_code == HTTPStatus.NO_CONTENT


def test_registration():
    email = 'eve.holt@reqres.in'
    password = '111'
    res = api.registration(email, password)

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json())


def test_registration_fail():
    email = 'eve.holt@reqres.in'

    res = api.registration_fail(email)
    res_body = res.json()
    assert res.status_code == HTTPStatus.BAD_REQUEST
    example = {
                "error": "Missing password"
              }
    assert res_body == example



