from django import forms 
from .models import UserProfileModel


TAG_CHOICES = [
    ('EN', 'Entertainment'), 
    ('EN2', 'Entertaintment 2'),
    ('EN3', 'Entertaintment 3'),
    ('EN4', 'Entertaintment 4'),
    ('EN5', 'Entertaintment 5'),
]


class UserProfileForm(forms.ModelForm):
    tags = forms.ChoiceField(choices=TAG_CHOICES)
    class Meta():
        model = UserProfileModel
        fields = '__all__'