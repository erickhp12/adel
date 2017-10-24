from django.db import models
from pacientes.models import Paciente
from empleados.models import Empleado
from django.db.models import permalink
from django.contrib.auth.models import User 

TIPOS_DIVISAS = (("Pesos", "Pesos"),("Dolares", "Dolares"))
TIPOS_PAGO = (("Efectivo", "Efectivo"),("Tarjeta", "Tarjeta"),
            ("Cheque", "Cheque"),("Transferencia bancaria", "Transferencia bancaria"),
            ("Pendiente", "Pendiente"))

class Visitas(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_visita = models.DateTimeField(verbose_name=u'Fecha')
    motivo = models.CharField(max_length=300, default='',null=True, unique=False, verbose_name=u'motivo')
    dentista = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,unique=False,verbose_name=u'Precio')
    dolares = models.CharField(max_length=50,choices=TIPOS_DIVISAS,null=True,unique=False,verbose_name=u'Divisas')
    tipo_pago = models.CharField(max_length=50,choices=TIPOS_PAGO,null=True,unique=False,verbose_name=u'tipo de pago')

    @permalink
    def url_ver_visitas(self):
        return ('ver_visita', [int(self.pk)])

    @permalink
    def url_editar_visitas(self):
        return ('editar_visita', [int(self.pk)])

    @permalink
    def url_borrar_visitas(self):
        return ('borrar_visita', [int(self.pk)])