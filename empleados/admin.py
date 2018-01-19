from django.contrib import admin
from . import models as m

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','direccion','fecha_inicio')
    list_filter = ('nombre',)
    search_fields = ['nombre']

admin.site.register(m.Empleado, EmpleadoAdmin)