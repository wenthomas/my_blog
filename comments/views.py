from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.
def post_comment(request, post_pk):
    #获取文章数据

    post = get_object_or_404(Post, pk = post_pk)

    #Http请求有get和post两种，一般用户通过表单提交数据都是通过post请求
    #因此只有当用户的请求为post时才需要处理表单数据
    if request.method == 'POST':
        #用户提交的数据存在request.POST中，这是一个类字典对象
        #我们利用这些数据构造了CommentForm的实例，这样Django的表单就生成了
        form = CommentForm(request.POST)

        #当调用form.is_valid()方法时，Django自动帮我们检查表单的数据是否符合格式要求
        if form.is_valid():
            #检查到数据是合法的，调用表单的save方法保存数据到数据库
            #commit = False的作用是仅仅利用表单的数据生成Comment模型类的实例，但还不保存评论数据到数据库
            comment = form.save(commit=False)

            #将评论和被评论的文章关联起来
            comment.post = post

            #最终将评论数据保存进数据库，调用模型实例的save方法
            comment.save()

            #重定向到post的详情页，实际上当redirect函数接收一个模型的实例时，它会调用这个模型实例的get_absolute_url方法
            #然后重定向到get_absolute_url方法返回的URL
            return redirect(post)

        else:
            #检查到数据不合法，重新渲染详情页，并且渲染表单的错误
            #因此我们传了三个模板变量到detail.html
            #一个是文章Post，一个是评论列表，一个是表单form
            #注意这里我们用到了post.comment_set.all()方法
            #这个用法有点类似于post.object.all()
            #其作用是获取这篇post下的全部评论，
            #因为Post和Comment是ForeignKey关联的，因此使用post.comment_set.all()反向查询所有评论
            #此处等效于Comment.objects.filter(post=post)
            comment_list = post.comment_set.all()
            context = {'post':post,
                       'form':form,
                       'comment_list':comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    #不是post请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(post)   #若redirect接收了post模型实例作为参数，则这个post必须已经实现了get_absolute_url这类url定向方法才可使用

