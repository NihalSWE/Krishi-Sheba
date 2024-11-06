<<<<<<< HEAD
from django import forms
from .models import F_Data

class ContactForm(forms.ModelForm):
    class Meta:
        model = F_Data
        fields = ['Name', 'Number', 'Email', 'Details']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'Number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'Details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 4}),
        }
=======
from ast import arg
from django import forms
from .models import F_Data
class ContactForm(forms.ModelForm):
    class Meta:
        model=F_Data
        fields='__all__'
>>>>>>> origin/master
