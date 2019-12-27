import requests
from .readutil import ReadConfig
from flask import current_app

gl_localReadConfig = ReadConfig()


class HttpUtil:
    def __init__(self):
        global host, port, timeout
        host = gl_localReadConfig.get_http("base_url")
        port = gl_localReadConfig.get_http("port")
        timeout = gl_localReadConfig.get_http("timeout")
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response.json()
        except TimeoutError:
            current_app.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, data=self.data, headers=self.headers, files=self.files,
                                     timeout=float(timeout))
            # response.raise_for_status()
            return response.json()
        except TimeoutError:
            current_app.logger.error("Time out!")
            return None
