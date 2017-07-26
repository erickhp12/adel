from django.contrib import admin
from . import models as m

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombres','puesto' ,'telefono','correo','direccion','fecha_inicio')
    list_filter = ('nombres',)
    search_fields = ['nombre']

admin.site.register(m.Empleado, EmpleadoAdmin)
