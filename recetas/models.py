from django.db import models
from pacientes.models import Paciente
from empleados.models import Empleado
from django.db.models import permalink
from django.contrib.auth.models import User 


class Recetas(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100, default='',null=True, unique=False, verbose_name=u'motivo')
    comentario = models.CharField(max_length=500, default='',null=True, unique=False, verbose_name=u'comentario')
    dentista = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_receta = models.DateTimeField(verbose_name=u'Fecha')
    
    @permalink
    def url_ver_recetas(self):
        return ('ver_receta', [int(self.pk)])

    @permalink
    def url_editar_recetas(self):
        return ('editar_receta', [int(self.pk)])