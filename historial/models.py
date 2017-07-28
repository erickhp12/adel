from __future__ import unicode_literals
from django.db import models
from pacientes.models import Paciente
from django.db.models import permalink

class Historial(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	sexo = models.CharField(max_length=10, null=True, verbose_name=u'sexo')
	estado_civil = models.CharField(max_length=20, null=True, verbose_name=u'estado civil')
	ocupacion = models.CharField(max_length = 30, null = True, verbose_name=u'ocupacion')
	alergias = models.BooleanField(default=False,verbose_name= u"Es alergico a alguna droga,anestesia,antibiotico?")
	corazon = models.BooleanField(default=False,verbose_name=u"Enfermedades del corazon")
	presion_arterial = models.BooleanField(default=False, verbose_name=u"Presion arterial")
	diabetes = models.BooleanField(default=False, verbose_name=u"Diabetes")
	hepatitis = models.BooleanField(default=False,verbose_name = u"Hepatitis")
	vih = models.BooleanField(default=False, verbose_name = u"Es usted portador del VIH")
	embarazada = models.BooleanField(default=False, verbose_name = u"si es mujer, Esta usted embarazada")
	medicamentos = models.BooleanField(default=False,verbose_name =u"Actualmente toma algun medicamento")

	class Meta:
		verbose_name = "Historial"
		verbose_name_plural = "Historiales"

	def __unicode__(self):
		return "%s" % (self.paciente.nombres)

