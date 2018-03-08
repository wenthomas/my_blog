from django.conf.urls import url
from . import views

#step6:编写url并关联视图函数views.py
app_name = 'blog'   #该行告诉django这个urls.py是属于blog应用的（视图函数命名空间），以区分其他app可能重复的index等视图函数，
urlpatterns = [
    url(r'^$', views.index, name = 'index'),     #r'^$'表示该http请求以空字符串开始且结尾
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name = 'detail'),  #P<pk>主键后跟至少1位数，例如post/1/或者post/255/,[0-9]+表示一位数或多位数，(?P<pk>[0-9]+)匹配的内容传递给views.detail方法


]