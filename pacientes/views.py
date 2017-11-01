from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from .models import Paciente
from visitas.models import Visitas
from historial.models import Historial
from .forms import RegistrarPaciente
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PacienteSerializer


class PatientListView(ListView):
    template_name = "pacientes.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        total = Paciente.objects.filter(user=request.user)
        total_pacientes = total.count()
        mensaje = ""

        if total_pacientes == 0:
            mensaje = "No tienes pacientes registrados"

        context = {'Paciente':total,
                    'total':total_pacientes,
                    'mensaje':mensaje     
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente_input = request.POST.get('paciente')
        mensaje = ""
        paciente = Paciente.objects.all().filter(nombre__icontains=paciente_input,user=request.user
                ) | Paciente.objects.all().filter(tipo_paciente__icontains=paciente_input,user=request.user
                ) | Paciente.objects.all().filter(aseguranza__icontains=paciente_input,user=request.user)
        total_paciente = paciente.count()

        if total_paciente == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = {'Paciente':paciente,
                    'total':total_paciente,
                    'mensaje': mensaje,
                    }
        
        return render(self.request, self.template_name, context)

class CreatePatientView(CreateView):
    template_name = "creacion_pacientes.html"
    template_main = "pacientes.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        pacientes = Paciente.objects.filter(user=request.user)
        total_pacientes = pacientes.count
        form = RegistrarPaciente()
        mensaje = ""
        context = {'pacientes': pacientes,
                   'total_pacientes': total_pacientes,
                   'form':form,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        pacientes = Paciente.objects.filter(user=request.user)
        total_pacientes = pacientes.count
        user = request.user
        nombre = request.POST.get('nombre')
        sexo = request.POST.get('sexo')
        edad = request.POST.get('edad')
        tipo_paciente = request.POST.get('tipo_paciente')
        aseguranza = request.POST.get('aseguranza')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        comentarios = request.POST.get('comentarios')

        # print "USER"
        # print user
        # print "Nombre"
        # print nombre
        # print "sexo"
        # print sexo
        # print "Edad"
        # print edad
        # print "tipo_paciente"
        # print tipo_paciente
        # print "aseguranza"
        # print aseguranza
        # print "telefono"
        # print telefono
        # print "correo"
        # print correo
        # print "direccion"
        # print direccion
        # print "comentarios"
        # print comentarios
        

        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                Paciente.objects.create(
                    user=user,
                    nombre=nombre,
                    sexo=sexo,
                    edad=edad,
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
                   'total_pacientes': total_pacientes,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.pacientes')


class UpdatePatientView(UpdateView):
    template_name = "edicion_paciente.html"

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
        total_pacientes = pacientes.count
        user = request.user
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
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
                paciente.edad = edad
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
                   'total_pacientes': total_pacientes,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.pacientes')


class DetailPatientView(DetailView):
    model = Paciente
    template_name = "paciente_detalle.html"

    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.get(id=pk)
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
        mensaje = ""
        total = Paciente.objects.filter(user=request.user)
        total_pacientes = total.count
        Paciente.objects.all().filter(id=pk).delete()

        context = {'Paciente':total,
                    'total':total_pacientes,
                    'mensaje':mensaje     
                    }

        return render(self.request,'pacientes.html', context)


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
