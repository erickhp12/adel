from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from visitas.models import Visitas
from historial.models import Historial
from .models import Paciente
from .forms import RegistrarPaciente
from .serializers import PacienteSerializer
import datetime

class PatientListView(ListView):
    template_name = "pacientes.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.filter(user=request.user).order_by('-fecha_inicio')
        total = pacientes.count()
        mensaje = ""

        if total == 0:
            mensaje = "No tienes pacientes registrados"

        context = {'pacientes':pacientes,
                    'total':total,
                    'mensaje':mensaje     
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente_input = request.POST.get('paciente')
        mensaje = ""

        pacientes = Paciente.objects.all().filter(nombre__icontains=paciente_input,user=request.user
                ) | Paciente.objects.all().filter(tipo_paciente__icontains=paciente_input,user=request.user
                ) | Paciente.objects.all().filter(aseguranza__icontains=paciente_input,user=request.user).order_by('-fecha_inicio')
        total = pacientes.count()

        if total == 0:
            mensaje = "No tienes pacientes registrados"

        context = {'pacientes':pacientes,
                    'total':total,
                    'mensaje':mensaje     
                    }
        
        return render(self.request, self.template_name, context)


class CreatePatientView(CreateView):
    template_name = "paciente-formulario.html"
    template_main = "pacientes.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        pacientes = Paciente.objects.filter(user=request.user)
        total = pacientes.count
        form = RegistrarPaciente()
        now = datetime.datetime.now()
        currentYear = now.year
        years = []
        year = 1940

        while currentYear >= year:
            years.append(currentYear)
            currentYear-=1

        mensaje = ""
        
        context = {
                    'pacientes': pacientes,
                    'years':years,
                    'total': total,
                    'form':form,
                    'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        pacientes = Paciente.objects.filter(user=request.user)
        total = pacientes.count
        user = request.user
        nombre = request.POST.get('nombre')
        sexo = request.POST.get('sexo')
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')
        tipo_paciente = request.POST.get('tipo_paciente')
        aseguranza = request.POST.get('aseguranza')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        comentarios = request.POST.get('comentarios')   
        birth = year + "-" + month + "-" + day

        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                Paciente.objects.create(
                    user=user,
                    nombre=nombre,
                    sexo=sexo,
                    fecha_nacimiento=birth,
                    tipo_paciente=tipo_paciente,
                    aseguranza=aseguranza,
                    telefono=telefono,
                    correo=correo,
                    direccion=direccion,
                    comentarios=comentarios
                )
        except Exception as e:
            mensaje = "Error al crear paciente " + str(e)

        context = {'pacientes': pacientes,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.pacientes')


class UpdatePatientView(UpdateView):
    template_name = "paciente-formulario.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        paciente = Paciente.objects.get(user=request.user,id=pk)
        form = RegistrarPaciente()
        mensaje = ""
        context = {'paciente': paciente,
                    'form':form,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        pacientes = Paciente.objects.filter(user=request.user)
        total = pacientes.count
        user = request.user
        nombre = request.POST.get('nombre')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        sexo = request.POST.get('sexo')
        tipo_paciente = request.POST.get('tipo_paciente')
        aseguranza = request.POST.get('aseguranza')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        contacto = request.POST.get('contacto')
        comentarios = request.POST.get('comentarios')

        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                paciente = Paciente.objects.get(user=request.user,id=pk)
                paciente.nombre = nombre
                paciente.fecha_nacimiento = fecha_nacimiento
                paciente.sexo = sexo
                paciente.tipo_paciente = tipo_paciente
                paciente.aseguranza = aseguranza
                paciente.telefono = telefono
                paciente.correo = correo
                paciente.direccion = direccion
                paciente.comentarios = comentarios
                paciente.save()
        except Exception as e:
            mensaje = "Error al editar paciente " + str(e)

        context = {'Paciente': pacientes,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.pacientes')


class DetailPatientView(DetailView):
    model = Paciente
    template_name = "paciente_detalle.html"

    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.get(id=pk)
        visitas = Visitas.objects.filter(paciente_id=pk)
        message = "Registrar historia clinica"
        historial = Historial.objects.all()
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

            print "Historial 1"
            ObjectHistorial = Historial.objects.filter(paciente_id=paciente.pk)
            print "Historial 2"
                
            print message

            for historial in ObjectHistorial:
                print "dentro de for"
                print historial.alergias_comentarios
                message = "si tiene historia clinica"

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
        except Exception as e:
            print "SI ENTRE ERROR"

        for visita in visitas:
            if visita.dolares == "Dolares":
                precio_dolares += visita.precio * settings.DIVISA
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
        mensaje = ""
        total = Paciente.objects.filter(user=request.user)
        total = total.count
        Paciente.objects.all().filter(id=pk).delete()

        context = {'Paciente':total,
                    'total':total,
                    'mensaje':mensaje     
                    }

        return render(self.request,'pacientes.html', context)

class requestSinglePatient(APIView):
    def get(self, request, pk, format=None):
        snippets = Paciente.objects.get(id=pk)
        serializer = PacienteSerializer(snippets, many=False)
        return Response(serializer.data)



class RequestPatients(APIView):
    def get(self, request, format=None):
        snippets = Paciente.objects.all()
        serializer = PacienteSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Response": "Paciente agregado correctamente"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_302_FOUND)
