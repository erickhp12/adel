# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from historial.serializers import HistorialSerializer
from historial.models import Historial
from pacientes.models import Paciente
from visitas.models import Visitas
from .forms import RegistrarHistorial
from django.core.urlresolvers import reverse_lazy

class RequestHistorial(APIView):
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, format=None):
        snippets = Historial.objects.all()
        serializer = HistorialSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HistorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Answer": 1}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_302_FOUND)


class CreateHistoryView(CreateView):
    template_name = "historial-formulario.html"
    template_main = "pacientes.html"
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.get(id=pk)
        historial_paciente = ""

        context = {
                    'historial_paciente':historial_paciente,
                    'paciente':paciente
                  }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        total = Paciente.objects.filter(user=request.user).order_by('-fecha_inicio')
        total_pacientes = total.count
        mensaje = ""
        paciente = request.POST.get('paciente')
        paciente_id = Paciente.objects.get(nombre=paciente)
        estado_civil = request.POST.get('estado_civil')
        ocupacion = request.POST.get('ocupacion')
        alergias = request.POST.get('alergias', False)
        alergias_comentarios = request.POST.get('alergias_comentarios')
        corazon = request.POST.get('corazon')
        presion_arterial = request.POST.get('presion_arterial')
        diabetes = request.POST.get('diabetes')
        hepatitis = request.POST.get('hepatitis')
        vih = request.POST.get('vih')
        embarazada = request.POST.get('embarazada')
        medicamentos = request.POST.get('medicamentos')
        medicamentos_comentarios = request.POST.get('medicamentos_comentarios')


        if alergias is None:
            alergias = 0
        if corazon is None:
            corazon = 0
        if presion_arterial is None:
            presion_arterial = 0
        if diabetes is None:
            diabetes = 0
        if hepatitis is None:
            hepatitis = 0
        if vih is None:
            vih = 0
        if embarazada is None:
            embarazada = 0
        if medicamentos is None:
            medicamentos = 0

        Historial.objects.create(paciente=paciente_id,
                        estado_civil=estado_civil,
                        ocupacion=ocupacion,
                        alergias=alergias,
                        alergias_comentarios=alergias_comentarios,
                        corazon=corazon,
                        presion_arterial=presion_arterial,
                        diabetes=diabetes,
                        hepatitis=hepatitis,
                        vih=vih,
                        embarazada=embarazada,
                        medicamentos=medicamentos,
                        medicamentos_comentarios=medicamentos_comentarios)


        context = { 
                    'Paciente':total,
                    'total':total_pacientes,
                    'mensaje':mensaje
                    }

        return render(self.request, self.template_main, context)

class EditHistoryView(CreateView):
    template_name = "historial-formulario.html"
    template_main = "pacientes.html"
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.get(id=pk)
        historial_paciente = Historial.objects.get(paciente_id=pk)
        alergias_comentarios_value = ""
        medicamentos_comentarios_value = ""
        alergias_value = "unchecked"
        corazon_value = "unchecked"
        presion_arterial_value = "unchecked"
        diabetes_value = "unchecked"
        hepatitis_value = "unchecked"
        vih_value = "unchecked"
        embarazada_value = "unchecked"
        medicamentos_value = "unchecked"

        alergias_comentarios_value = historial_paciente.alergias_comentarios
        medicamentos_comentarios_value = historial_paciente.medicamentos_comentarios
        if historial_paciente.alergias == True:
            alergias_value = "checked"
        if historial_paciente.corazon == True:
            corazon_value = "checked"
        if historial_paciente.presion_arterial == True:
            presion_arterial_value = "checked"
        if historial_paciente.diabetes == True:
            diabetes_value = "checked"
        if historial_paciente.hepatitis == True:
            hepatitis_value = "checked"
        if historial_paciente.vih == True:
            vih_value = "checked"
        if historial_paciente.embarazada == True:
            embarazada_value = "checked"
        if historial_paciente.medicamentos == True:
            medicamentos_value = "checked"



        context = {
                    'paciente':paciente,
                    'historial_paciente':historial_paciente,
                    'alergias_value':alergias_value,
                    'alergias_comentarios_value':alergias_comentarios_value,
                    'corazon_value':corazon_value,
                    'presion_arterial_value':presion_arterial_value,
                    'diabetes_value':diabetes_value,
                    'hepatitis_value':hepatitis_value,
                    'vih_value':vih_value,
                    'embarazada_value':embarazada_value,
                    'medicamentos_value':medicamentos_value,
                    'medicamentos_comentarios_value':medicamentos_comentarios_value,
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        pacientes = Paciente.objects.filter(user=request.user).order_by('-fecha_inicio')
        total_pacientes = pacientes.count
        mensaje = ""
        paciente = request.POST.get('paciente')
        paciente_id = Paciente.objects.filter(nombre=paciente).first()
        estado_civil = request.POST.get('estado_civil')
        ocupacion = request.POST.get('ocupacion')
        alergias = request.POST.get('alergias', False)
        alergias_comentarios = request.POST.get('alergias_comentarios')
        corazon = request.POST.get('corazon')
        presion_arterial = request.POST.get('presion_arterial')
        diabetes = request.POST.get('diabetes')
        hepatitis = request.POST.get('hepatitis')
        vih = request.POST.get('vih')
        embarazada = request.POST.get('embarazada')
        medicamentos = request.POST.get('medicamentos')
        medicamentos_comentarios = request.POST.get('medicamentos_comentarios')


        if alergias is None:
            alergias = 0
            alergias_comentarios = ""
        if corazon is None:
            corazon = 0
        if presion_arterial is None:
            presion_arterial = 0
        if diabetes is None:
            diabetes = 0
        if hepatitis is None:
            hepatitis = 0
        if vih is None:
            vih = 0
        if embarazada is None:
            embarazada = 0
        if medicamentos is None:
            medicamentos = 0
            medicamentos_comentarios = ""


        nuevo_historial_paciente = Historial.objects.get(paciente_id=paciente_id)
        nuevo_historial_paciente.estado_civil = estado_civil
        nuevo_historial_paciente.ocupacion = ocupacion
        nuevo_historial_paciente.alergias = alergias
        nuevo_historial_paciente.alergias_comentarios = alergias_comentarios
        nuevo_historial_paciente.corazon = corazon
        nuevo_historial_paciente.presion_arterial = presion_arterial
        nuevo_historial_paciente.diabetes = diabetes 
        nuevo_historial_paciente.hepatitis = hepatitis
        nuevo_historial_paciente.vih = vih
        nuevo_historial_paciente.embarazada = embarazada
        nuevo_historial_paciente.medicamentos = medicamentos
        nuevo_historial_paciente.medicamentos_comentarios = medicamentos_comentarios
        nuevo_historial_paciente.save()

        context = { 
                    'pacientes':pacientes,
                    'total':total_pacientes,
                    'mensaje':mensaje
                    }

        return render(self.request, self.template_main, context)

