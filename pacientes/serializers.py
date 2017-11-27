from rest_framework import serializers

from pacientes.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
            'User',
            'nombre',
            'sexo',
            'edad',
            'tipo_paciente',
            'aseguranza',
            'telefono',
            'correo',
            'direccion',
            'comentarios',
        )
