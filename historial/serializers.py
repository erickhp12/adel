from rest_framework import serializers

from historial.models import Historial


class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = (
            'paciente',
            'estado_civil',
            'ocupacion',
            'alergias',
            'alergias_comentarios',
            'corazon',
            'presion_arterial',
            'diabetes',
            'hepatitis',
            'vih',
            'embarazada',
            'medicamentos',
            'medicamentos_comentarios'
        )
