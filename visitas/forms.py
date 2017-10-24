from django.forms import ModelForm
from django import forms
from .models import Visitas
from django.forms import TextInput


class RegistrarVisita(ModelForm):
    class Meta:
        model = Visitas
        exclude = []
        
        widgets = {
            'tipo_pago': forms.Select(attrs={'class': 'form-control'}),
            'dolares': forms.Select(attrs={'class': 'form-control'})}