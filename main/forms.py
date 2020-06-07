from django import forms
from .models import Comment

# コメント投稿
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "sex", "age", "text", )
        widgets = {
            "name": forms.TextInput(attrs={"class": "comment_name", "placeholder": "Input your name"}),
            "text": forms.Textarea(attrs={"placeholder": "Please comment here"}),
            "age": forms.NumberInput(attrs={"class": "comment_age"}),
        }

# 記事検索
class PostSearchForm(forms.Form):
    keyword = forms.CharField(
        required = False,
        widget = forms.TextInput(
            attrs={"class": "search_input", "placeholder": "keyword search"}
        ),
    )
