from django.db import models
from pacientes.models import Paciente
from empleados.models import Empleado
from django.db.models import permalink

TIPOS_DIVISAS = (("Pesos", "Pesos"),("Dolares", "Dolares"))
TIPOS_PAGO = (("Efectivo", "Efectivo"),("Tarjeta", "Tarjeta"),("Cheque", "Cheque"))

class Visitas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_visita = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha de visita')
    motivo = models.CharField(max_length=300, default='',null=True, unique=False, verbose_name=u'motivo')
    dentista = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    precio = models.CharField(max_length=50,default='',null=True,unique=False,verbose_name=u'Precio')
    dolares = models.CharField(max_length=50,choices=TIPOS_DIVISAS,verbose_name=u'Divisa')
    tipo_pago = models.CharField(max_length=50,choices=TIPOS_PAGO,null=True,unique=False,verbose_name=u'tipo de pago')

    # def __str__(self):
    #     return self.nombres

    @permalink
    def url_ver(self):
        return ('ver_visita', [int(self.pk)])

    @permalink
    def url_editar(self):
        return ('editar_visita', [int(self.pk)])