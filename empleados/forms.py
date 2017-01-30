from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import TextInput

class EmployeeForm(forms.ModelForm):
    nombres = forms.CharField(label='nombres', widget=forms.TextInput(attrs={'required':'true'}))
    apellidos = forms.CharField(label='apellidos', widget=forms.TextInput(attrs={'required':'true'}))
    puesto = forms.CharField(label='puesto', widget=forms.TextInput(attrs={'required':'true'}))
    telefono = forms.CharField(label='telefono', widget=forms.TextInput(attrs={'required':'true'}))
    correo = forms.EmailField(label='correo', widget=forms.TextInput(attrs={'required':'true'}))