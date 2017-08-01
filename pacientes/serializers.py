from rest_framework import serializers

from pacientes.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
            'nombres',
            'apellidos',
            'edad',
            'tipo_paciente',
            'aseguranza',
            'telefono',
            'correo',
            'direccion',
            'comentarios',
        )
