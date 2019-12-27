#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os
import json
import ddt
import base64
from innowealth.libs.log import Log
from innowealth.libs.httputil import HttpUtil
from innowealth.libs.excelutil import Excel
from innowealth.libs.tools import GetRequestParas,Sign
from innowealth.libs.rsautil import sign_with_privakey

"""
初始化EXCEL数据
"""
project_dir = os.path.dirname(os.path.abspath('.'))
excelPath = project_dir + '/data/test_data.xlsx'
"""如果测试单个test"""
# excelPath = project_dir + '/data/login.xlsx'
PerformanceBondSheetName = "performance_bond"
pb_excel = Excel(excelPath)
pb_excel_data = pb_excel.get_list(PerformanceBondSheetName)

data = {"performanceType": "1", "size": "3", "service": "performance_bond", "signType": "MD5", "language": "zh",
        "symbol": "7a2bebea12dc34d8a735e1f4c0d3e55a", "sign": "dc1942d59542a97f252386b232537870"}


@ddt.ddt
class Performance_Bond(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_driver = HttpUtil()
        cls.log = Log()

    @classmethod
    def tearDownClass(cls):
        pass

    @ddt.data(*pb_excel_data)
    def test_performance_bond(self, data):
        """债券主题"""
        data['sign'] = Sign.get_sign(data)
        self.http_driver.set_url('')
        self.http_driver.set_headers({'Content-Type': 'application/json'})
        self.http_driver.set_data(json.dumps(data, ensure_ascii=False).encode('utf-8'))
        self.log.info(self.http_driver.data)
        response = self.http_driver.post()
        self.log.info(response)
        assert response.get('responseCode') == 'SUCCESS'


if __name__ == '__main__':
    unittest.main()
