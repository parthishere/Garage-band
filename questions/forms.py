from django.forms import forms
from .models import Questions

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question','image']
