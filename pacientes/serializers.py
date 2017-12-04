from rest_framework import serializers

from pacientes.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        # fields = (
        #     'user',
        #     'nombre',
        #     'sexo',
        #     'edad',
        #     'tipo_paciente',
        #     'aseguranza',
        #     'telefono',
        #     'correo',
        #     'direccion',
        #     'comentarios',
        # )


class singlePacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'