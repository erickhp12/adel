from django.forms import ModelForm
from django import forms
from .models import Empleado
from django.forms import TextInput 

# class RegistrarEmpleado(ModelForm):
#     class Meta:
#         model = Empleado
#         exclude = []
        # widget = {
        #     'nombres': TextInput(
        #         attrs={'autofocus': '','class': 'form-control'}
        #     ),
        #     'telefono': TextInput(
        #     	attrs={'placeholder':'telefono!'})
        # }

class RegistrarEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        exclude = []
        fields =['nombre','puesto','edad','telefono','correo','direccion']
        widget = {
            'telefono': TextInput(
                attrs={'placeholder':'telefono'}
                )
            }

