from django.db import models
from django.core.urlresolvers import reverse

class Empleado(models.Model):
    nombres = models.CharField(max_length=200,null=False, unique=True, verbose_name=u'nombres')
    apellidos = models.CharField(max_length=200, null=False, unique=False, verbose_name=u'apellidos')
    puesto = models.CharField(max_length=100, null=False, unique=False, verbose_name=u'puesto')
    telefono = models.CharField(max_length=100, null=True, unique=False, verbose_name=u'telefono')
    correo = models.EmailField(max_length=100, null=True, unique=True, verbose_name=u'correo')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')

    def __str__(self):
        return self.nombres + ' - ' + self.apellidos
