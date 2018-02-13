# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, View
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from .models import Agenda
from pacientes.models import Paciente
from empleados.models import Empleado
from django.http import HttpResponseRedirect
from visitas.models import Visitas
from .forms import RegistrarAgenda
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import time 


class AgendaListView(ListView):
    template_name = "agenda.html" 

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        fecha_inicial = time.strftime("%Y-%m-%d")
        fecha_final = time.strftime("%Y-%m-%d")
        estado = 0
        mensaje = ""
        agenda = Agenda.objects.filter(user=request.user).order_by('-fecha_agenda')
        total = agenda.count()

        if total == 0:
            mensaje = "No tienes citas para el rango de fechas seleccionado, checa en otro horario"

        context = {
                    'agenda':agenda,
                    'total':total,
                    'estado':estado,
                    'fecha_inicial':fecha_inicial,
                    'fecha_final':fecha_final,
                    'mensaje': mensaje      
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs): 
        dia = time.strftime("%Y-%m-%d")
        fecha_inicial = time.strftime("%Y-%m-%d")
        busqueda = request.POST.get('busqueda')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final') 
        mensaje = ""


        if fecha_final and fecha_final != "":
            agenda = Agenda.objects.filter(
                fecha_agenda__range=[fecha_inicial, fecha_final + " 23:59:59"],user=request.user)
        else:
            agenda = Agenda.objects.filter(empleado__nombre__icontains=busqueda,user=request.user
                ) | Agenda.objects.filter(paciente__nombre__icontains=busqueda,user=request.user
                ) | Agenda.objects.filter(motivo__icontains=busqueda,user=request.user).order_by('-fecha_agenda')
        total = agenda.count()

        if total == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = {'agenda':agenda,
                    'total':total,
                    'fecha_inicial':fecha_inicial,
                    'fecha_final':fecha_final,
                    'mensaje': mensaje
                    }
        
        return render(self.request, self.template_name, context)

class CreateAgendaView(View):
    template_name = "agenda-formulario.html"
    
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.filter(user=request.user).order_by('nombre')
        empleados = Empleado.objects.filter(user=request.user).order_by('nombre')
        fecha_inicial = time.strftime("%Y-%m-%d")
        
        context = { 
                    'fechai':fecha_inicial,
                    'pacientes': pacientes,
                    'empleados':empleados
                }

        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        fecha_inicial = time.strftime("%Y-%m-%d")
        fecha_final = time.strftime("%Y-%m-%d")
        visitas = Agenda.objects.all().filter(fecha_agenda__range=[fecha_inicial, fecha_final + " 23:59:59"]).order_by('fecha_agenda')
        total_visitas = visitas.count()
        user = request.user
        pacienteSeleccionado = request.POST.get('paciente')
        paciente = Paciente.objects.filter(nombre=pacienteSeleccionado).first()
        motivo = request.POST.get('motivo')
        empleadoSeleccionado = request.POST.get('empleado')
        empleado = Empleado.objects.filter(nombre=empleadoSeleccionado).first()
        fecha_agenda = request.POST.get('fecha')

        try:
            if paciente == "":
                return render(self.request, self.template_name)
            else:
                Agenda.objects.create(
                    user=user,
                    empleado=empleado,
                    paciente=paciente,
                    motivo=motivo,
                    fecha_agenda=fecha_agenda
                )
        except Exception as e:
            mensaje = "Error al crear visita " + str(e)

        context = {
                    'visitas': visitas,
                    'total_visitas': total_visitas,
                    'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.agenda')


class UpdateAgendaView(UpdateView):
    template_name = "agenda-formulario.html"
    
    def get(self, request, pk, *args, **kwargs):
        agenda = Agenda.objects.get(id=pk) 
        pacientes = Paciente.objects.filter(user=request.user).order_by('nombre')
        empleados = Empleado.objects.filter(user=request.user).order_by('nombre')
        fecha_inicial = time.strftime("%Y-%m-%d")

        ctx = {
                'agenda': agenda,
                'pacientes':pacientes,
                'fecha_inicial':fecha_inicial,
                'empleados':empleados
                }

        return render(request,self.template_name,ctx)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        fecha_inicial = time.strftime("%Y-%m-%d")
        fecha_final = time.strftime("%Y-%m-%d")
        visitas = Agenda.objects.all().filter(fecha_agenda__range=[fecha_inicial, fecha_final + " 23:59:59"]).order_by('fecha_agenda')
        total_visitas = visitas.count()
        user = request.user
        pacienteSeleccionado = request.POST.get('paciente')
        paciente = Paciente.objects.filter(nombre=pacienteSeleccionado).first()
        motivo = request.POST.get('motivo')
        empleadoSeleccionado = request.POST.get('empleado')
        empleado = Empleado.objects.filter(nombre=empleadoSeleccionado).first()
        fecha_agenda = request.POST.get('fecha') 

        try:
            if paciente == "":
                return render(self.request, self.template_name)
            else:
                agenda = Agenda.objects.get(user=request.user,id=pk)
                agenda.paciente = paciente
                agenda.motivo = motivo
                agenda.empleado = empleado
                agenda.motivo = motivo
                agenda.fecha_agenda = fecha_agenda
                agenda.save()
        except Exception as e:
            mensaje = "Error al editar cita " + str(e)

        context = {
                    'visitas': visitas,
                    'total_visitas': total_visitas,
                    'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.agenda')   


class DeleteAgendaView(ListView):
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):
        Agenda.objects.filter(id=pk,user=request.user).delete()

        return render(request,'agenda.html')