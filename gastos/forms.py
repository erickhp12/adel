from django.forms import ModelForm
from django import forms
from .models import Gasto
from . import models


class RegistrarGasto(ModelForm):
    class Meta:
        model = models.Gasto
        exclude = []

        widgets = {
            'tipo_pago': forms.Select(attrs={'class': 'form-control'}),
            'dolares': forms.Select(attrs={'class': 'form-control'})}