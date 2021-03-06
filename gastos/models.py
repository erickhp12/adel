from django.db import models
from proveedores.models import Proveedor
from empleados.models import Empleado
from django.db.models import permalink
from django.contrib.auth.models import User 

TIPOS_DIVISAS = (("Pesos", "Pesos"),("Dolares", "Dolares"))
TIPOS_PAGO = (("Efectivo", "Efectivo"),("Tarjeta", "Tarjeta"),
            ("Cheque", "Cheque"),("Transferencia bancaria", "Transferencia bancaria")
            ,("Pendiente", "Pendiente"))

class Gasto(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=300, default='',null=True, unique=False, verbose_name=u'motivo')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,unique=False,verbose_name=u'Precio')
    dolares = models.CharField(max_length=50,choices=TIPOS_DIVISAS,verbose_name=u'Divisa')
    tipo_pago = models.CharField(max_length=50,choices=TIPOS_PAGO,null=True,unique=False,verbose_name=u'tipo de pago')
    fecha_gasto = models.DateTimeField(verbose_name=u'fecha de gasto')
    

    @permalink
    def url_editar_gasto(self):
        return ('editar_gasto', [int(self.pk)])

    @permalink
    def url_borrar_gasto(self):
        return ('borrar_gasto', [int(self.pk)])