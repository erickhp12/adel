from django.contrib import admin
from . import models as m

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('paciente','motivo' ,'fecha_agenda')
    list_filter = ('paciente',)
    search_fields = ['paciente']

admin.site.register(m.Agenda, AgendaAdmin)