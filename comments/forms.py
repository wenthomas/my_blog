from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment #引用内部类Meta中设计好的的评论模型
        fields = ['name', 'email', 'url', 'text']

