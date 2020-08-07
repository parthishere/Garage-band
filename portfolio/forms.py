from django import forms 
from .models import UserProfileModel
from allauth.account.forms import SignupForm


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta():
        model = UserProfileModel
        fields = (
            'dob', 
            'phone_no', 
            'profession', 
            'about', 
            'softwear', 
            'image', 
            'photography', 
            'music', 
            'video', 
            'awards', 
            'first_name', 
            'last_name', 
            'tags'
        )

    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user.profile.nationality = self.cleaned_data['nationality']
        user.profile.gender = self.cleaned_data['bio']
        user.profile.save()

