# -*- coding:utf-8 -*-
# @Author : Dummerfu
# @Contact : https://github.com/dummerchen 
# @Time : 2021/4/22 15:03
from django.conf.urls import url,include
from . import views
urlpatterns=[
    url(r'^',views.Index_View.as_view(),name='contents'),
]