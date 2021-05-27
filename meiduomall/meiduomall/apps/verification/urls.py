# -*- coding:utf-8 -*-
# @Author : Dummerfu
# @Contact : https://github.com/dummerchen 
# @Time : 2021/4/29 13:52

from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'image_codes/(?P<uuid>.+)/$',views.Capture_View.as_view()),
    url(r'verify_image_code/$',views.Image_Code_View.as_view(),name='check_image_code'),
    url(r'sms_codes/$',views.Sms_Code_View.as_view()),
]