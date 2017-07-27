from django.forms import ModelForm
from django import forms
from .models import Empleado
from django.forms import TextInput


class RegistrarEmpleado(ModelForm):
    class Meta:
        model = Empleado
        exclude = []
        widget = {
            'nombres': TextInput(
                attrs={'autofocus': '','class': 'form-control'}
            )
        }
