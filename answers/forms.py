from django import forms
from .models import Answers, Comment

class PostAnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        exclude = ['user', 'question', 'like', 'dislike', 'slug', 'like_count', 'dislike_count']

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'slug', 'answer',]
