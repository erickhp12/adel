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
    template_name = "creacion_historial.html"
    template_main = "pacientes.html"
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.get(id=pk)


        context = {'paciente':paciente}

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        total = Paciente.objects.all()
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

        print "paciente"
        print paciente
        print "estado_civil "
        print estado_civil
        print "ocupacion "
        print ocupacion
        print "alergias "
        print alergias
        print "alergias comentarios"
        print alergias_comentarios
        print "corazon "
        print corazon
        print "presion_arterial "
        print presion_arterial
        print "diabetes "
        print diabetes
        print "hepatitis "
        print hepatitis
        print "vih "
        print vih
        print "embarazada"
        print embarazada
        print "medicamentos"
        print medicamentos
        print "medicamentos comentarios"
        print medicamentos_comentarios

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


        context = { 'Paciente':total,
                    'total':total_pacientes,
                    'mensaje':mensaje
                    }

        return render(self.request, self.template_main, context)
