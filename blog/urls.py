from django.conf.urls import url
from . import views

#step6:编写url并关联视图函数views.py
urlpatterns = [
    url(r'^$', views.index, name = 'index')     #r'^$'表示该http请求以空字符串开始且结尾
]