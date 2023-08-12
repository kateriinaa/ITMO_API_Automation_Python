import json
from api.client import Client


class HttpBinApi(Client):
    IP = '/ip'
    ROBOTS = '/robots.txt'
    HTML = '/html'
    BASE_URL = 'https://httpbin.org'
    TIME = '/delay'

    def list_html(self):
        url = self.BASE_URL + self.HTML
        return self.get(url)

    def robots(self):
        url = self.BASE_URL + self.ROBOTS
        return self.get(url)

    def ip(self):
        url = self.BASE_URL + self.IP
        return self.get(url)

    def time_out(self, delay=1):
        url = self.BASE_URL + self.TIME + f'/3'
        try:
            return self.get(url, timeout=delay)
        except Exception as ex:
            return False, ex


http_bin_api = HttpBinApi()