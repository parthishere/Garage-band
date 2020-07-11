from django.forms import ModelForm
from .models import Questions

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question','image','like']
