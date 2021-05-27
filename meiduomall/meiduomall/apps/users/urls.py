from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'username/(?P<username>[a-zA-Z0-9_-]{5,20})/$',views.Username_View.as_view(),name='check_username'),
    url(r'mobile/(?P<mobile>1[4-9]\d{9})/$',views.Username_View.as_view(),name='check_mobile'),
    url(r'^',views.Register_View.as_view(),name='register'),
]
