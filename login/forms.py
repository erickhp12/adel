# coding=utf-8

from django import forms
from django.forms.widgets import TextInput

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario',
                               widget=forms.TextInput(attrs={'required':'True'}))
    password = forms.CharField(label='Contraseña',
                               widget=forms.PasswordInput(attrs={'required':'True'}))
