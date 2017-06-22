from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, View
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from .models import Agenda
from pacientes.models import Paciente
from .forms import RegistrarAgenda
import time


class AgendaListView(ListView):
    queryset = Agenda.objects.all().order_by('fecha_agenda')
    template_name = "agenda.html"

    def get(self, request, *args, **kwargs):
        total = Agenda.objects.all()
        total_agenda = Agenda.objects.all().count
        
        context = {'Agenda':total,
                    'total_agenda':total_agenda,        
                    }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente = request.POST.get('paciente')
        total_agenda = Agenda.objects.all().filter(paciente__nombres__contains=paciente
            ) | Agenda.objects.all().filter(paciente__apellidos__contains=paciente)
        total = total_agenda.count()

        context = {'Agenda':total_agenda,'total_agenda':total}
        
        return render(self.request, self.template_name, context)

class CreateAgendaView(View):
    template_name = "creacion_agenda.html"
    
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.all()
        
        ctx = {'pacientes': pacientes}

        return render(request,self.template_name,ctx)

    def post(self, request, *args, **kwargs):
        fecha_agenda = request.POST.get('fecha')
        paciente_id = request.POST.get('paciente')
        paciente = Paciente.objects.get(pk=paciente_id)
        motivo = request.POST.get('motivo')
        fecha_agenda += " 00:00:00"

        Agenda.objects.create(paciente=paciente,motivo=motivo, fecha_agenda=fecha_agenda)

        context = {'ingresos':fecha_agenda}

        return render(self.request, self.template_name, context)

class UpdateAgendaView(UpdateView):
    template_name = "edicion_agenda.html"
    
    def get(self, request, *args, **kwargs):
        id =kwargs.get('pk')
        pacientes = Agenda.objects.get(pk=id) 

        ctx = {'paciente': pacientes}

        return render(request,self.template_name,ctx)

    # def post(self, request, *args, **kwargs):
    #     fecha_agenda = request.POST.get('fecha')
    #     paciente_id = request.POST.get('paciente')
    #     paciente = Paciente.objects.get(pk=paciente_id)
    #     motivo = request.POST.get('motivo')
    #     fecha_agenda += " 00:00:00"

    #     Agenda.objects.create(paciente=paciente,motivo=motivo, fecha_agenda=fecha_agenda)

    #     context = {'ingresos':fecha_agenda}

    #     return render(self.request, self.template_name, context)   


class DetailAgendaView(DetailView):
    model = Agenda
    template_name = "agenda_detalle.html"


 

