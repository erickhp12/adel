from django.contrib import admin
from . import models as m

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','sexo','tipo_paciente','aseguranza','telefono','correo','direccion','fecha_inicio')
    list_filter = ('nombre',)
    search_fields = ['nombre']

admin.site.register(m.Paciente, PacienteAdmin)