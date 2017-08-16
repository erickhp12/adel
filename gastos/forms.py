from django.forms import ModelForm
from django import forms
from .models import Gasto
from django.forms import TextInput


class RegistrarGasto(ModelForm):
    class Meta:
        model = Gasto
        exclude = []
        widgets = {
            'fecha_gasto': TextInput(
                attrs={'id': 'datepicker'}
            )
        }