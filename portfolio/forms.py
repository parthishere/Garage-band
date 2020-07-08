from django.forms import forms, ModelForm

from allauth.account.forms import SignupForm 
from .models import UserProfileModel
  
class CustomSignupForm(SignupForm, ModelForm):
    username = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(null=True, blank=True) 
    
    class Meta():
        model = UserProfileModel
        fields = ['username', 'email', 'date_of_birth']
    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.email = self.cleaned_data['email']
        user.save()