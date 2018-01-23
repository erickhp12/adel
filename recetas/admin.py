from django.contrib import admin
from . import models as m

class RecetaAdmin(admin.ModelAdmin):
    list_display = ('paciente' ,'dentista','comentario','fecha_receta')
    list_filter = ('paciente',)
    search_fields = ['paciente']

admin.site.register(m.Recetas, RecetaAdmin)
