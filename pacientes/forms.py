from django.forms import ModelForm
from django import forms
from .models import Paciente
from django.forms import TextInput


class RegistrarPaciente(ModelForm):
    class Meta:
        model = Paciente
        exclude = []
        widget = {
            'nombres': TextInput(
                attrs={'autofocus': '','class': 'form-control'}
            )
        }
