from django.forms import forms
from .models import Answers

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        field = ['answer','image','like']
