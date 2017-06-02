from django.db import models
from django.db.models import permalink

TIPOS_PACIENTES = (("Particular", "Particular"),("Aseguranza", "Aseguranza"))

class Paciente(models.Model):
    nombres = models.CharField(max_length=100, null=False, unique=True, verbose_name=u'nombre(s)')
    apellidos = models.CharField(max_length=100, null=False, unique=False, verbose_name=u'apellido(s)')
    tipo_paciente = models.CharField(max_length=100, choices=TIPOS_PACIENTES,null=False, unique=False, verbose_name=u'tipo paciente')
    aseguranza = models.CharField(max_length=100, default='',null=True, unique=False, verbose_name=u'aseguranza')
    telefono = models.CharField(max_length=100, null=True, unique=False, verbose_name=u'telefono')
    correo = models.EmailField(max_length=100, null=True, unique=True, verbose_name=u'correo')
    direccion = models.CharField(max_length=200,default='',null=True,unique=False,verbose_name=u'Direccion')
    comentarios = models.CharField(max_length=500,default='',null=True,unique=False,verbose_name=u'Comentarios')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    @permalink
    def url_ver_paciente(self):
        return ('ver_paciente', [int(self.pk)])

    @permalink
    def url_editar_paciente(self):
        return ('editar_paciente', [int(self.pk)])