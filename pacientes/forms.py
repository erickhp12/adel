from django.forms import ModelForm
from django import forms
from .models import Paciente
from django.forms import TextInput


class RegistrarPaciente(ModelForm):
    class Meta:
        model = Paciente
        exclude = []
        widget = {
            'aseguranza': TextInput(
                attrs={'value': 'no aplica','placeholder': 'no aplica'}
            )
        }
