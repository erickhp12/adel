from django.forms import ModelForm
from django import forms
from .models import Visitas
from django.forms import TextInput


class RegistrarVisita(ModelForm):
    class Meta:
        model = Visitas
        exclude = []
        widget = {
            'nombres': TextInput(
                attrs={'autofocus': '','class': 'form-control'}
            )
        }