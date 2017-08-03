from django.forms import ModelForm
from django import forms
from .models import Historial
from django.forms import TextInput


class RegistrarHistorial(ModelForm):
    class Meta:
        model = Historial
        exclude = []
        widget = {
            'nombres': TextInput(
                attrs={'autofocus': '','class': 'form-control'}
            )
        }