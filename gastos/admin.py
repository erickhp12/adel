from django.contrib import admin
from . import models as m

class GastoAdmin(admin.ModelAdmin):
    list_display = ('proveedor','empleado' ,'motivo','precio','dolares','tipo_pago','fecha_gasto')
    list_filter = ('motivo',)
    search_fields = ['motivo']

admin.site.register(m.Gasto, GastoAdmin)