from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User

class Empleado(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=False, unique=False,verbose_name=u'nombre(s)')
    puesto = models.CharField(max_length=100, null=False, unique=False, verbose_name=u'puesto')
    edad = models.IntegerField(null=True, unique=False, verbose_name='Edad')
    telefono = models.CharField(max_length=15, null=True, unique=False, verbose_name=u'telefono')
    correo = models.EmailField(max_length=100, null=True, unique=False, verbose_name=u'correo')
    direccion = models.CharField(max_length=200,null=True,unique=False,verbose_name=u'Direccion')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')

    def __str__(self):
        return self.nombre

    @permalink
    def url_editar_empleado(self):
        return ('editar_empleado', [int(self.pk)])

    @permalink
    def url_borrar_empleado(self):
        return ('borrar_empleado', [int(self.pk)])
