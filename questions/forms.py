from django import forms
from .models import Questions

class QuestionForm(forms.ModelForm):
    """ Question Model Form """
    class Meta():
        model = Questions
        exclude=['user',]