from django.forms import ModelForm
from django import forms
from .models import Empleado
from django.forms import TextInput 

class RegistrarEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        exclude = []
        fields =['nombre','puesto','fecha_nacimiento','telefono','correo','direccion']
        widget = {
            'telefono': TextInput(
                attrs={'placeholder':'telefono'}
                )
            }

