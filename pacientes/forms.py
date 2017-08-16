from django.forms import ModelForm
from django import forms
from .models import Paciente
from django.forms import TextInput


class RegistrarPaciente(ModelForm):
    class Meta:
        model = Paciente
        exclude = []
        widgets = {
            'aseguranza': TextInput(
                attrs={'placeholder': 'asdfasdfasd'}
            ),
            'edad': TextInput(
            	attrs={'placeholder':'hola','class':'txtInput'}
            )
        }

    
