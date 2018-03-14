import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
from comments.forms import CommentForm


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

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk) #此处的pk等价于文章id

    #阅读量+1
    post.increase_views()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ]
                                  )

    form = CommentForm()

    #获取这篇post下的全部评论
    comment_list = post.comment_set.all()

    #将文章、表单、以及文章下的评论列表作为模板变量传递给detail.html
    context = {'post':post,
               'form':form,
               'comment_list':comment_list
               }
    return render(request, 'blog/detail.html',context=context)

#归档页面详情
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html',context={'post_list':post_list})

#分类页面详情
def category(request, pk):
    cate = get_object_or_404(Category, pk = pk) #判断数据是否存在，存在则取出，不存在则返回404
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})