from django.db import models
from pacientes.models import Paciente
from empleados.models import Empleado
from django.db.models import permalink
from django.contrib.auth.models import User 

TIPO_CONFIRMACION = (("Pendiente", "Pendiente"),("Confirmada", "Confirmada"),("Cancelada","Cancelada"))
class Agenda(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	motivo = models.CharField(max_length=300, default='',null=True, unique=False, verbose_name=u'motivo')
	confirmacion = models.CharField(max_length=15,choices=TIPO_CONFIRMACION, default='Pendiente',null=True,unique=False,verbose_name=u'tipo de pago')
	fecha_agenda = models.DateTimeField(auto_now_add=False, verbose_name=u'fecha programada')

	@permalink
	def url_editar_agenda(self):
		return ('editar_agenda', [int(self.pk)])

	@permalink
	def url_borrar_agenda(self):
		return ('borrar_agenda', [int(self.pk)])