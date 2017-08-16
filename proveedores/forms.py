from django.forms import ModelForm
from django import forms
from .models import Proveedor
from django.forms import TextInput


class RegistrarProveedor(ModelForm):
    class Meta:
        model = Proveedor
        exclude = []
        widgets = {
            'nombre': TextInput(
                attrs={'autofocus': '','placeholder': ''}
            )
        }
