#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from innowealth.api_1_0 import api
from flask import Flask, current_app
from innowealth.libs.log import Log
from innowealth.libs.httputil import HttpUtil
import json


class SaltValue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_driver = HttpUtil()
        cls.log = Log()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_salt_value(self):
        data = {'language': 'zh',
                'service': 'salt_value',
                'sign': '5be649e5eb420286bb8adfe45cfcf044',
                'signType': 'MD5',
                'symbol': 'c693453d6dc59fedd5a9bb01960c8cb6',
                'uticket': ''
                }
        self.http_driver.set_url('')
        self.http_driver.set_headers({'Content-Type': 'application/json'})
        self.http_driver.set_data(json.dumps(data, ensure_ascii=False))
        response = self.http_driver.post()
        self.log.info(response)
        # current_app.logger.info(response)
        assert response.get('responseCode') == 'SUCCESS'

    # def test_get_salt_value(self):
    #     params = {'language': 'zh',
    #               'service': 'salt_value',
    #               'sign': '5be649e5eb420286bb8adfe45cfcf044',
    #               'signType': 'MD5',
    #               'symbol': 'c693453d6dc59fedd5a9bb01960c8cb6',
    #               'uticket': ''}
    #     self.http_driver.set_url('/api/user')
    #     self.http_driver.set_params(json.dumps(params, ensure_ascii=False))
    #     response = self.http_driver.get()


if __name__ == '__main__':
    unittest.main()
