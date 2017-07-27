from django.contrib import admin
from . import models as m

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos','tipo_paciente','aseguranza','telefono','correo','direccion','fecha_inicio')
    list_filter = ('nombres',)
    search_fields = ['nombres']

admin.site.register(m.Paciente, PacienteAdmin)