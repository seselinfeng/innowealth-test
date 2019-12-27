#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from innowealth.libs.log import Log
from innowealth.libs.httputil import HttpUtil
import json


class Home_Banner_List(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_driver = HttpUtil()
        cls.log = Log()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_home_banner_list(self):
        """banner列表"""
        data = {
            "service": "home_banner_list",
            "signType": "MD5",
            "language": "zh",
            "symbol": "7a2bebea12dc34d8a735e1f4c0d3e55a",
            "sign": "6179e9068610427019ef1bf708088ccf"
        }
        self.http_driver.set_url('')
        self.http_driver.set_headers({'Content-Type': 'application/json'})
        self.http_driver.set_data(json.dumps(data, ensure_ascii=False))
        response = self.http_driver.post()
        self.log.info(response)
        assert response.get('responseCode') == 'SUCCESS'


if __name__ == '__main__':
    unittest.main()
