from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

#step7:编写视图函数，完成请求处理并返回数据
#step8:编写模板文件返回用户正确的页面
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'title':'托马斯的个人小站',
        'post_list':post_list
    })
    #测试首页：
    # #return render(request, 'blog/index.html', context={
    #    'title':'我的博客首页',
    #   'welcome':'欢迎访问我的博客首页！'
    #接到http请求时寻找'blog/index.html'模板文件，并且通过context参数传入相应的变量