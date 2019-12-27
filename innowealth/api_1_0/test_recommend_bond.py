#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from innowealth.libs.log import Log
from innowealth.libs.httputil import HttpUtil
import json


class Recommend_Bond(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_driver = HttpUtil()
        cls.log = Log()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_recommend_bond(self):
        """推荐债券"""
        data = {
            "recommendType": "1",
            "service": "recommend_bond",
            "signType": "MD5",
            "language": "zh",
            "symbol": "7a2bebea12dc34d8a735e1f4c0d3e55a",
            "sign": "56a1ea8cafe2bfa59147d7f1752eef00"
        }
        self.http_driver.set_url('')
        self.http_driver.set_headers({'Content-Type': 'application/json'})
        self.http_driver.set_data(json.dumps(data, ensure_ascii=False))
        response = self.http_driver.post()
        self.log.info(response)
        assert response.get('responseCode') == 'SUCCESS'


if __name__ == '__main__':
    unittest.main()
