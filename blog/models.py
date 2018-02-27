
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#分类表:分类名
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

#标签表：标签名
class Tags(models.Model):
    name = models.CharField(max_length=100)

#文章表：标题、正文、创建时间、更改时间、摘要、分类（FK）、标签（FK）、作者（FK）
class Post(models.Model):
    """文章标题"""
    title = models.CharField(max_length=70)

    #文章正文：Textfield，常用于长文本
    body = models.TextField()

    #创建时间和修改时间
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要：可以没有摘要，指定CharField的 blank=True 参数后可以允许空值
    excerpt = models.CharField(max_length=200, blank=True)

    #FK：关联分类表、标签表(ManyToManyField:多对多类型）
    category = models.ForeignKey(to="Category",to_field="name",on_delete=models.CASCADE)
    #on_delete=models.CASCADE)级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除

    tags = models.ManyToManyField(Tags,blank=True)

    #文章作者：User表是从django.contrib.auth.models导入的，为内置应用，专门处理网站用户的注册、登录等流程，User是Django为我们写好的用户模型
    author = models.ForeignKey(User,on_delete=models.CASCADE)
