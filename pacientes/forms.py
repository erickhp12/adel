from django.forms import ModelForm
from django import forms
from .models import Paciente
from django.forms import TextInput


class RegistrarPaciente(ModelForm):
    class Meta:
        model = Paciente
        exclude = []
        widgets = {
            'tipo_paciente': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'sexo': forms.Select(
                attrs={'class': 'form-control'}
            )
        }
