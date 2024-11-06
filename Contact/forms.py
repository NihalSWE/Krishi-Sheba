from ast import arg
from django import forms
from .models import F_Data
class ContactForm(forms.ModelForm):
    class Meta:
        model=F_Data
        fields='__all__'