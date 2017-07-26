from django.db import models
from pacientes.models import Paciente
from django.db.models import permalink

class Agenda(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=300, default='',null=True, unique=False, verbose_name=u'motivo')
    fecha_agenda = models.DateTimeField(auto_now_add=False, verbose_name=u'fecha programada')
    estado = models.CharField(max_length=50, default='',null=True, unique=False, verbose_name=u'estado')

    @permalink
    def url_ver_agenda(self):
        return ('ver_agenda', [int(self.pk)])

    @permalink
    def url_editar_agenda(self):
        return ('editar_agenda', [int(self.pk)])

    @permalink
    def url_borrar_agenda(self):
        return ('borrar_agenda', [int(self.pk)])