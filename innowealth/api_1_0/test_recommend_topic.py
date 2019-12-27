#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from innowealth.libs.log import Log
from innowealth.libs.httputil import HttpUtil
import json


class Recommend_Topic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_driver = HttpUtil()
        cls.log = Log()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_recommend_topic(self):
        """推荐主题"""
        data = {
            "service": "recommend_topic",
            "signType": "MD5",
            "language": "zh",
            "symbol": "7a2bebea12dc34d8a735e1f4c0d3e55a",
            "sign": "9674f3259d494827b27177b92503b008"
        }
        self.http_driver.set_url('')
        self.http_driver.set_headers({'Content-Type': 'application/json'})
        self.http_driver.set_data(json.dumps(data, ensure_ascii=False))
        response = self.http_driver.post()
        self.log.info(response)
        assert response.get('responseCode') == 'SUCCESS'


if __name__ == '__main__':
    unittest.main()
