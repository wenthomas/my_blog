
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
#step4:models.py配置数据库
#step5:搭建数据库并迁移数据库完成python到数据库语言的转化，实现数据库修改
#分类表:分类名
class Category(models.Model):

    """该构造器方法用于将数据内容在取数据的过程中返回显示出来"""
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)

#标签表：标签名
class Tags(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)

#文章表：标题、正文、创建时间、更改时间、摘要、分类（FK）、标签（FK）、作者（FK）
class Post(models.Model):

    def __str__(self):
        return self.title
    """文章标题"""

    #自定义get_absolute_url方法，并从django.urls中导入reverse函数
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk}) #reverse函数返回的是blog应用下name=detail的url

    title = models.CharField(max_length=70)

    #文章正文：Textfield，常用于长文本
    body = models.TextField()

    #创建时间和修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要：可以没有摘要，指定CharField的 blank=True 参数后可以允许空值
    excerpt = models.CharField(max_length=200, blank=True)

    #FK：关联分类表、标签表(ManyToManyField:多对多类型）
    category = models.ForeignKey(to="Category",to_field="name", on_delete=models.CASCADE)
    #on_delete=models.CASCADE)级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除

    tags = models.ManyToManyField(Tags, blank=True)

    #文章作者：User表是从django.contrib.auth.models导入的，为内置应用，专门处理网站用户的注册、登录等流程，User是Django为我们写好的用户模型
    author = models.ForeignKey(User, on_delete=models.CASCADE)
