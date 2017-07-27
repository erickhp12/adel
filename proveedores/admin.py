from django.contrib import admin
from . import models as m

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre','contacto','telefono','correo','direccion','producto','fecha_inicio')
    list_filter = ('nombre',)
    search_fields = ['nombre']

admin.site.register(m.Proveedor, ProveedorAdmin)