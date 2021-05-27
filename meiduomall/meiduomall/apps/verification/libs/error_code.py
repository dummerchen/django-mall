# -*- coding:utf-8 -*-
# @Author : Dummerfu
# @Contact : https://github.com/dummerchen 
# @Time : 2021/5/5 10:43

class Error_Code():
    def __init__(self):
        self.error_code_json={
            "验证码错误":4003,
            "验证码过期":4001,
            "未知错误":4004,
        }

    def error_code(self,text):
        return self.error_code_json[text]
