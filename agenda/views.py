# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, View
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from .models import Agenda
from pacientes.models import Paciente
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
        total = Agenda.objects.all().filter(fecha_agenda__range=[fecha_inicial, fecha_final + " 23:59:59"]).order_by('fecha_agenda')
        total_agenda = total.count()

        if total_agenda == 0:
            mensaje = "No tienes citas para hoy, checa en otro horario"
        context = {'Agenda':total,
                    'total_agenda':total_agenda,
                    'estado':estado,
                    'fecha_inicial':fecha_inicial,
                    'fecha_final':fecha_final,
                    'mensaje': mensaje      
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs): 
        dia = time.strftime("%Y-%m-%d")
        paciente = request.POST.get('paciente')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final') 
        mensaje = ""

        if paciente == "" and fecha_inicial == "" and fecha_final == "":
            total_agenda = Agenda.objects.all().filter(fecha_agenda__range=[dia, dia + " 23:59:59"]).order_by('fecha_agenda')
            total = total_agenda.count()
        elif paciente == "":
            fecha_final = fecha_final
            total_agenda = Agenda.objects.all().filter(fecha_agenda__range=[fecha_inicial, fecha_final + " 23:59:59"])
            total = total_agenda.count()
        else:
            total_agenda = Agenda.objects.all().filter(paciente__nombre__icontains=paciente)
            total = total_agenda.count()

        if total == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = {'Agenda':total_agenda,
                    'total_agenda':total,
                    'fecha_inicial':fecha_inicial,
                    'fecha_final':fecha_final,
                    'mensaje': mensaje
                    }
        
        return render(self.request, self.template_name, context)

class CreateAgendaView(View):
    template_name = "creacion_agenda.html"
    
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.all()
        fecha_inicial = time.strftime("%Y-%m-%d")
        ctx = {'fechai':fecha_inicial,
                'pacientes': pacientes}

        return render(request,self.template_name,ctx)

    def post(self, request, *args, **kwargs):
        fecha_inicial = time.strftime("%Y-%m-%d")
        fecha_final = time.strftime("%Y-%m-%d")
        total = Agenda.objects.all().filter(fecha_agenda__range=[fecha_inicial, fecha_final + " 23:59:59"]).order_by('fecha_agenda')
        total_agenda = total.count()
        mensaje = ""
        fecha_agenda = request.POST.get('fecha')
        hora_agenda = request.POST.get('hora')
        paciente_id = request.POST.get('paciente')
        paciente = Paciente.objects.get(pk=paciente_id)
        motivo = request.POST.get('motivo')

        Agenda.objects.create(paciente=paciente,motivo=motivo, fecha_agenda=fecha_agenda)

        context = {'Agenda':total,
                    'mensaje':mensaje,
                    'total_agenda':total_agenda,
                    'ingresos':fecha_agenda}

        return render(self.request, "agenda.html", context)

class UpdateAgendaView(UpdateView):
    template_name = "edicion_agenda.html"
    
    def get(self, request, pk, *args, **kwargs):
        pacientes = Agenda.objects.get(id=pk) 

        ctx = {'paciente': pacientes}

        return render(request,self.template_name,ctx)


class DetailAgendaView(DetailView):
    model = Agenda
    template_name = "agenda_detalle.html"


class DeleteAgendaView(ListView):
    template_name = "eliminar_agenda.html"

    def get(self, request, pk, **kwargs):
        agenda = Agenda.objects.all().filter(id=pk)

        context = {'agenda':agenda}

        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        Agenda.objects.all().filter(id=pk).delete()
        return render(self.request,'agenda.html')


 

