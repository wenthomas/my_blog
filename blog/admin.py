from django.contrib import admin
from .models import Post, Category, Tags

# Register your models here.
#step10:配置后台模型
#将Post, Category, Tags添加到admin后台管理界面中

#该方法用于定制admin后台显示效果
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tags)
