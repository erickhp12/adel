from django.forms import ModelForm
from django import forms
from .models import Agenda
from django.forms import TextInput

class RegistrarAgenda(ModelForm):
    class Meta:
        model = Agenda
        exclude = []
        widget = {
            'paciente': TextInput(
                attrs={'autofocus': '','class': 'form-control'}
            )
        }
