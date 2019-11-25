from django.contrib.auth import password_validation
from django.contrib.auth.forms import UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext, gettext_lazy as _


class LoginForm(forms.Form):
    """
    Simple login form
    """
    username = forms.CharField(max_length=25, label="Имя пользователя")
    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    """
    Simple registration form
    """

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput, max_length=50)
    password = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput, max_length=50)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
        field_classes = {'username': UsernameField}

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cleaned_data['password2']
