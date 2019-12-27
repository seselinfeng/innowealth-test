#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from innowealth.libs.log import Log
from innowealth.libs.httputil import HttpUtil
import json


class Login_Pass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_driver = HttpUtil()
        cls.log = Log()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_login_pass(self):
        """用户登录"""
        data = {
            "identityId": "15000000121",
            "platformType": "android",
            "password": "33ec6e196065ba20be685558c850bc6058bf3815970af043a60e893c1276e9a0",
            "firebaseToken": "Aux32CelDDv_vwpmDXY6Z_y2bBuUxXf4_NGb3vMuWwtk",
            "service": "login_pass",
            "signType": "MD5",
            "language": "zh",
            "symbol": "7a2bebea12dc34d8a735e1f4c0d3e55a",
            "sign": "835c6b83a05f35943e5eae400bdd1432"
        }
        self.http_driver.set_url('')
        self.http_driver.set_headers({'Content-Type': 'application/json'})
        self.http_driver.set_data(json.dumps(data, ensure_ascii=False))
        response = self.http_driver.post()
        self.log.info(response)
        assert response.get('responseCode') == 'SUCCESS'


if __name__ == '__main__':
    unittest.main()
