from django.contrib import admin
from . import models as m

class VisitaAdmin(admin.ModelAdmin):
    list_display = ('paciente','motivo' ,'dentista','precio','dolares','tipo_pago','fecha_visita',)
    list_filter = ('paciente',)
    search_fields = ['paciente']

admin.site.register(m.Visitas, VisitaAdmin)
