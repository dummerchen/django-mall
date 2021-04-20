# -*- coding:utf-8 -*-
# @Author : Dummerfu
# @Contact : https://github.com/dummerchen 
# @Time : 2021/4/20 18:16

from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

def jinja2_env(**options):
    env=Environment(**options)
    env.globals.update({
        'static':staticfiles_storage.url, # 获取静态文件前缀
        'url':reverse, # 反向解析路由
    })
    return env

