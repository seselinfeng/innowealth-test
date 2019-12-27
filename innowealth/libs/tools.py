#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import rsautil
import sys
import inspect
import base64



class GetCurrentItems(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        pass

    @staticmethod
    def get_current_file_path():
        return __file__

    def get_current_class_name(self):
        return self.__class__.__name__

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    @staticmethod
    def get_current_lineno():
        return sys._getframe().f_lineno


class GetRequestParas(object):
    """Request请求参数，排序并拼接"""

    @staticmethod
    def para_filter(**kwargs):
        sign_dict = {}
        for key in kwargs:
            if str(kwargs[key]) != '' and str(key) != 'sign' and str(key) != 'signType':
                sign_dict[key] = kwargs[key]
        return sorted(sign_dict.items(), key=lambda x: x[0])

    @staticmethod
    def create_link_string(sign_dict):
        pre_str = ''
        for key in sign_dict:
            pre_str = pre_str + str(key[0]) + '=' + str(key[1] + '&')
        else:
            pre_str = pre_str.rstrip('&')
        return pre_str


class Sign(object):
    """获取签名"""

    @staticmethod
    def get_sign(data):
        sign = GetRequestParas.para_filter(**data)
        sign = GetRequestParas.create_link_string(sign)
        sign = rsautil.sign_with_privakey(sign)
        return base64.b64encode(sign).decode()


if __name__ == '__main__':
    str_list = GetRequestParas.para_filter(service='user_profile', signType='MD5', language='zh',
                                           uticket='RE1xMjJqVGRESVklQCU2ZGE1ZjMwMmFkZTVkYzMyZDkxZmRkMzZmMGVjNTFmZiVAJTE4ODg4ODg4ODg4OSVAJTE1NjQ2NTIwNDA5MjQ=',
                                           symbol='7a2bebea12dc34d8a735e1f4c0d3e55a', sign='123')
    str = GetRequestParas.create_link_string(str_list)
    print(str)
