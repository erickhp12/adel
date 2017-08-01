from django.db import models
from django.db.models import permalink

class Proveedor(models.Model):
    nombre = models.CharField(max_length=150, null=False, unique=True, verbose_name=u'nombre(s)')
    contacto = models.CharField(max_length=150, null=False, unique=False, verbose_name=u'contacto(s)')
    telefono = models.CharField(max_length=15,null=True, unique=False, verbose_name=u'telefono')
    correo = models.EmailField(max_length=100,null=True, unique=False, verbose_name=u'correo')
    direccion = models.CharField(max_length=150, null=True, unique=False, verbose_name=u'direccion')
    producto = models.CharField(max_length=200, null=True, unique=True, verbose_name=u'productos/servicios')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')

    def __str__(self):
        return self.nombre + ' ' + self.contacto

    @permalink
    def url_editar_proveedor(self):
        return ('editar_proveedor', [int(self.pk)])

    @permalink
    def url_borrar_proveedor(self):
        return ('borrar_proveedor', [int(self.pk)])