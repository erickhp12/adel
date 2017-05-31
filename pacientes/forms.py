from django.forms import ModelForm
from django import forms
from .models import Paciente


class RegistrarPaciente(ModelForm):
    class Meta:
        model = Paciente
        nombres = forms.CharField(label='Nombre(s)'),
        apellidos = forms.CharField(label='Apellido(s)'),
        tipo_paciente = forms.CharField(label='tipo de paciente'),
        aseguranza = forms.CharField(label='aseguranza'),
        telefono = forms.CharField(label='Telefono'),
        correo = forms.EmailField(label='Correo'),
        direccion = forms.CharField(label='Direccion'),
        comentarios = forms.CharField(label='comentarios'),
        fields = '__all__'


def __unicode__(self):
    return "%s" % self.nombres
