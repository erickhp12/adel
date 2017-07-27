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
        total = Agenda.objects.all().filter(fecha_agenda__range=[fecha_inicial, fecha_final + " 23:59:59"]).order_by('fecha_agenda')
        total_agenda = total.count()

        context = {'Agenda':total,
                    'total_agenda':total_agenda,
                    'estado':estado,
                    'fecha_inicial':fecha_inicial,
                    'fecha_final':fecha_final        
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs): 
        dia = time.strftime("%Y-%m-%d")
        paciente = request.POST.get('paciente')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final') 

        if paciente == "" and fecha_inicial == "" and fecha_final == "":
            total_agenda = Agenda.objects.all().filter(fecha_agenda__range=[dia, dia + " 23:59:59"]).order_by('fecha_agenda')
            total = total_agenda.count()
        elif paciente == "":
            fecha_final = fecha_final
            total_agenda = Agenda.objects.all().filter(fecha_agenda__range=[fecha_inicial, fecha_final + " 23:59:59"])
            total = total_agenda.count()
        else:
            total_agenda = Agenda.objects.all().filter(paciente__nombres__icontains=paciente
                ) | Agenda.objects.all().filter(paciente__apellidos__icontains=paciente)
            total = total_agenda.count()

        context = {'Agenda':total_agenda,
                    'total_agenda':total,
                    'fecha_inicial':fecha_inicial,
                    'fecha_final':fecha_final}
        
        return render(self.request, self.template_name, context)

class CreateAgendaView(View):
    template_name = "creacion_agenda.html"
    
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.all()
        
        ctx = {'pacientes': pacientes}

        return render(request,self.template_name,ctx)

    def post(self, request, *args, **kwargs):

        fecha_agenda = request.POST.get('fecha')
        hora_agenda = request.POST.get('hora')
        paciente_id = request.POST.get('paciente')
        paciente = Paciente.objects.get(pk=paciente_id)
        motivo = request.POST.get('motivo')

        print "Paciente"
        print paciente
        print "fecha"
        print fecha_agenda
        print "hora"
        print hora_agenda
        fecha_agenda = fecha_agenda + " " + hora_agenda + ":00"
        print "fecha final"
        print fecha_agenda

        Agenda.objects.create(paciente=paciente,motivo=motivo, fecha_agenda=fecha_agenda)

        context = {'ingresos':fecha_agenda}

        return render(self.request, "agenda.html", context)

class UpdateAgendaView(UpdateView):
    template_name = "edicion_agenda.html"
    
    def get(self, request, *args, **kwargs):
        id =kwargs.get('pk')
        pacientes = Agenda.objects.get(pk=id) 

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


 

