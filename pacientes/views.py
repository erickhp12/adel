from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Paciente
from visitas.models import Visitas
from historial.models import Historial
from .forms import RegistrarPaciente
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PacienteSerializer
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PatientListView(ListView):
    template_name = "pacientes.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        total = Paciente.objects.all()
        total_pacientes = total.count
        mensaje = ""
        context = {'Paciente':total,
                    'total':total_pacientes,
                    'mensaje':mensaje     
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente_input = request.POST.get('paciente')
        mensaje = ""
        paciente = Paciente.objects.all().filter(nombre__icontains=paciente_input
                ) | Paciente.objects.all().filter(tipo_paciente__icontains=paciente_input
                ) | Paciente.objects.all().filter(aseguranza__icontains=paciente_input)
        total_paciente = paciente.count()

        if total_paciente == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = {'Paciente':paciente,
                    'total':total_paciente,
                    'mensaje': mensaje,
                    }
        
        return render(self.request, self.template_name, context)

class CreatePatientView(CreateView):
    form_class = RegistrarPaciente
    template_name = "creacion_pacientes.html"
    success_url = reverse_lazy('list_pacientes')


class UpdatePatientView(UpdateView):
    model = Paciente
    form_class = RegistrarPaciente
    template_name = "creacion_pacientes.html"
    success_url = reverse_lazy('list_pacientes')    


class DetailPatientView(DetailView):
    model = Paciente
    template_name = "paciente_detalle.html"

    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.all().filter(id=pk)
        visitas = Visitas.objects.all().filter(paciente_id=pk)
        historial = ""
        message = ""
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
        precio_pesos = 0
        precio_dolares = 0
        precio_total = 0

        try:
            historial = Historial.objects.get(paciente=pk)

            alergias_comentarios_value = historial.alergias_comentarios
            medicamentos_comentarios_value = historial.medicamentos_comentarios
            if historial.alergias == True:
                alergias_value = "checked"
            if historial.corazon == True:
                corazon_value = "checked"
            if historial.presion_arterial == True:
                presion_arterial_value = "checked"
            if historial.diabetes == True:
                diabetes_value = "checked"
            if historial.hepatitis == True:
                hepatitis_value = "checked"
            if historial.vih == True:
                vih_value = "checked"
            if historial.embarazada == True:
                embarazada_value = "checked"
            if historial.medicamentos == True:
                medicamentos_value = "checked"
        except:
            message = "Registrar historial"

        for visita in visitas:
            if visita.dolares == "Dolares":
                precio_dolares += visita.precio * settings.DIVISA
                print precio_dolares
            else:
                precio_pesos += visita.precio

        precio_total = precio_pesos + precio_dolares


        context = {'visitas':visitas,
                    'paciente':paciente,
                    'historial':historial,
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
                    'precio_total':precio_total,
                    'message':message,
                    }
        return render(request,self.template_name, context)


class DeletePatientView(ListView):
    template_name = "eliminar_paciente.html"

    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.all().filter(id=pk)

        context = {'paciente':paciente}

        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        Paciente.objects.all().filter(id=pk).delete()

        return render(self.request,'pacientes.html')


class RequestPaciente(APIView):
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, format=None):
        snippets = Paciente.objects.all()
        serializer = PacienteSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Response": "Agregado correctamente"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_302_FOUND)
