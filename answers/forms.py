from django import forms
from .models import Answers

class PostAnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        exclude = ['user', 'question_id', 'like	']