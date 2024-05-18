from django import forms
from .models import CandidateDetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    """
    Form for creating/editing user profile.
    """
    class Meta:
        model = CandidateDetails
        fields = ['name','age', 'exp','phone','email','education', 'domain', 'skills', 'technologies']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

