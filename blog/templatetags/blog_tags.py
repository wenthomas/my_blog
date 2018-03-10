from ..models import Post, Category
from django import template

#在Django 中注册该函数get_recent_posts为模板标签{% get_recent_posts %}
register = template.Library()

@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')
#.dates会返回一个列表，其中包含所有文章对象，并按照后面参数规定的时间进行排序，DESC表示为降序

@register.simple_tag
def get_recent_posts(num = 5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_categories():
    return Category.objects.all()