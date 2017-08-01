from django.db import models
from django.db.models import permalink 

class Empleado(models.Model):
    nombres = models.CharField(max_length=200, null=False, unique=False,verbose_name=u'nombre(s)')
    apellidos = models.CharField(max_length=200, null=False, unique=False, verbose_name=u'apellido(s)')
    puesto = models.CharField(max_length=100, null=False, unique=False, verbose_name=u'puesto')
    telefono = models.CharField(max_length=15, null=True, unique=False, verbose_name=u'telefono')
    correo = models.EmailField(max_length=100, null=True, unique=False, verbose_name=u'correo')
    direccion = models.CharField(max_length=200,null=True,unique=False,verbose_name=u'Direccion')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    @permalink
    def url_ver_empleado(self):
        return ('ver_empleado', [int(self.pk)])

    @permalink
    def url_editar_empleado(self):
        return ('editar_empleado', [int(self.pk)])

    @permalink
    def url_borrar_empleado(self):
        return ('borrar_empleado', [int(self.pk)])
