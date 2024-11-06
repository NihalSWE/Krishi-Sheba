from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from ProductItem.models import Customer

# Register Form
class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Confirm password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-input', 'placeholder': 'Enter email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Enter username'})}

# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-input', 'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Password'}))

# Password Change Form
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Old password'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'New password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Confirm new password'}))

# Password Reset Form
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control form-input', 'placeholder': 'Enter email'}))

# Set New Password Form
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'New password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Confirm new password'}))

# Customer Profile Form
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'locality', 'city', 'district', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Full name'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control form-input', 'placeholder': 'Phone number'}),
            'locality': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Locality'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'City'}),
            'district': forms.Select(attrs={'class': 'form-control form-input'}),
            'gender': forms.Select(attrs={'class': 'form-control form-input'})
        }