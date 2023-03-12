from django import forms
from .models import UserDb

class UserForm(forms.ModelForm):
    class Meta:
        model=UserDb
        fields='__all__'
