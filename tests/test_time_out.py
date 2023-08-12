import re
from utils.assertions import Assert
from api.httpbin_api import http_bin_api
from http import HTTPStatus


def test_time_out():

    res = http_bin_api.time_out(10)
    assert res.status_code == HTTPStatus.OK

    res = http_bin_api.time_out(2)
    assert res[0] == False
