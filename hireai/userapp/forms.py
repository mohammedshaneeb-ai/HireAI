from django import forms
from .models import CandidateDetails

class UserProfileForm(forms.ModelForm):
    """
    Form for creating/editing user profile.
    """
    class Meta:
        model = CandidateDetails
        fields = ['name','age', 'exp','email', 'domain', 'skills', 'technologies', 'resume_link']
