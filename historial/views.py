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
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.get(id=pk)
        print "quieres editar el historial de"
        print paciente
        print paciente.pk

        context = {'paciente':paciente}

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente = request.POST.get('visita')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final')

        if fecha_final and fecha_final != "":
            total_visitas = Visitas.objects.all().filter(fecha_visita__range=[fecha_inicial, fecha_final + " 23:59:59"])
        else:
            total_visitas = Visitas.objects.all().filter(paciente__nombres__icontains=paciente
                ) | Visitas.objects.all().filter(paciente__apellidos__icontains=paciente
                ) | Visitas.objects.all().filter(motivo__icontains=paciente)
        total = total_visitas.count()

        context = {'visitas':total_visitas,'total_visitas':total}
        
        return render(self.request, self.template_name, context)



