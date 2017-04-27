from django.forms import ModelForm
from django import forms
from .models import Empleado


class RegistrarEmpleado(ModelForm):
    class Meta:
        model = Empleado
        nombres = forms.CharField(label='Nombre(s)'),
        apellidos = forms.CharField(label='Apellido(s)'),
        puesto = forms.CharField(label='Puesto'),
        telefono = forms.CharField(label='Telefono'),
        correo = forms.EmailField(label='Correo'),
        fields = '__all__'


def __unicode__(self):
    return "%s" % self.nombres
