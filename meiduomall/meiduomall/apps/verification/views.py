from django.shortcuts import render
from django.views import View
from django import http
from capture import captcha
from django_redis import get_redis_connection

# Create your views here.

class Capture_View(View):

    def get(self,request,uuid):
        # 生成图片
        text,img=captcha.generate_captcha()
        # 保存图片到redis

        redis_connect=get_redis_connection('verify_code')
        redis_connect.setex('imgs_%s'%uuid,30000,text)
        # return http.JsonResponse({'image':img,'content_type':'image/jpg')
        return http.HttpResponse(content=img,content_type='image/jpg')

class Image_Code_View(View):
    def get(self,request):
        pic_code=request.GET.get('pic_code')
        uuid=request.GET.get('uuid')
        print('req',uuid)
        print('image_code_uuid',pic_code)

        redis_connect=get_redis_connection('verify_code')
        true_code=redis_connect.get('imgs_%s'%uuid)

        if (true_code==None):
            return http.JsonResponse({'code':4001,'error_msg':'验证码过期'})
        true_code=true_code.decode()
        if(true_code.lower()!=pic_code.lower()):
            return http.JsonResponse({'code':4001,'error_msg':'验证码错误'})


class Sms_Code_View(View):
    def get(self,request,mobile):
        pic_code=request.GET.get('pic_code')
        uuid=request.GET.get('uuid')
        # return http.JsonResponse({'error_msg':})
        return http.JsonResponse({'error_msg':'ohhh?'})
