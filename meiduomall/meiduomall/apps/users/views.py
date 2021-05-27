import re

import redis
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django import http
from .models import User
from django.db import DatabaseError
from django_redis import get_redis_connection
# Create your views here.
# 和用户相关的视图
class Username_View(View):
    def get(self,request,username):

        count=User.objects.filter(username=username).count()

        return http.JsonResponse({'count':count,'errormsg':'username ok','code':0})

class Mobile_View(View):
    def get(self,request,mobile):

        count=User.objects.filter(mobile=mobile).count()

        return http.JsonResponse({'count':count,'errormsg':'mobile ok','code':0})


class Register_View(View):
    '''
        用户注册
    '''
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):

        username=request.POST.get('user_name')
        password=request.POST.get('pwd')
        password2=request.POST.get('cpwd')
        phone=request.POST.get('phone')
        # 用户的输入

        msg_code=request.POST.get('msg_code')
        allow=request.POST.get('allow')


        if not all([username,password,password2,phone]):
            return http.HttpResponseForbidden('信息不齐全')

        # 用户名验证
        if not re.match(r'^[a-zA-z0-9_-]{5,20}$',username):
            return http.HttpResponseForbidden('用户名不符合规范')
        # check password
        if password2!=password:
            return http.HttpResponseForbidden('密码不一致')

        # check phone
        if not re.match(r'^1[3-9]\d{9}$',phone):
            return http.HttpResponseForbidden('手机号不规范')
        # check image_code

        if allow!='on':
            return http.HttpResponseForbidden('请同意条款')

        try:
            user=User.objects.create_user(username=username,password=password,mobile=phone)
        except DatabaseError:
            return render(request,'register.html',{'register_error':'用户名已存在'})

        login(request,user)
        return render(request,reverse('contents:index'))