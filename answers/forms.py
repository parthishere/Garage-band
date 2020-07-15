from django.forms import forms
from .models import Answers,Comment

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['answer','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
