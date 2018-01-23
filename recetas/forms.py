from django.forms import ModelForm
from django import forms
from .models import Recetas

class RegistrarReceta(ModelForm):
    class Meta:
        model = Recetas
        exclude = []