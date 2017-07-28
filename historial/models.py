from __future__ import unicode_literals
from django.db import models
from pacientes.models import Paciente
from django.db.models import permalink

TIPO_SEXO = (("Femenino", "Femenino"),("Masculino", "Masculino"))
TIPO_ESTADO_CIVIL = (("Soltero", "Soltero"),("Casado", "Casado"),("Otros", "Otros"))

class Historial(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	sexo = models.CharField(max_length=10, null=True,choices=TIPO_SEXO, verbose_name=u'sexo')
	estado_civil = models.CharField(max_length=20, null=True,choices=TIPO_ESTADO_CIVIL, verbose_name=u'estado civil')
	ocupacion = models.CharField(max_length = 50, null = True, verbose_name=u'ocupacion')
	alergias = models.BooleanField(default=False,verbose_name= u"Es alergico a alguna droga,anestesia,antibiotico?")
	alergias_comentarios = models.CharField(max_length=200,default='', unique=False,null=True, verbose_name='describa')
	corazon = models.BooleanField(default=False,verbose_name=u"Enfermedades del corazon")
	presion_arterial = models.BooleanField(default=False, verbose_name=u"Presion arterial")
	diabetes = models.BooleanField(default=False, verbose_name=u"Diabetes")
	hepatitis = models.BooleanField(default=False,verbose_name = u"Hepatitis")
	vih = models.BooleanField(default=False, verbose_name = u"Es usted portador del VIH")
	embarazada = models.BooleanField(default=False, verbose_name = u"si es mujer, Esta usted embarazada")
	medicamentos = models.BooleanField(default=False,verbose_name =u"Actualmente toma algun medicamento")
	medicamentos_comentarios = models.CharField(max_length=200,default='',unique=False, null=True, verbose_name='describa')

	class Meta:
		verbose_name = "Historial de pacientes"
		verbose_name_plural = "Historial de pacientes"

	def __unicode__(self):
		return "%s" % (self.paciente.nombres)

