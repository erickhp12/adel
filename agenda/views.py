from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from .models import Agenda
from .forms import RegistrarAgenda


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

class CreateAgendaView(CreateView):
    form_class = RegistrarAgenda
    template_name = "creacion_agenda.html"
    success_url = reverse_lazy('list_agenda')


class UpdateAgendaView(UpdateView):
    model = Agenda
    form_class = RegistrarAgenda
    template_name = "creacion_agenda.html"
    success_url = reverse_lazy('list_agenda')    


class DetailAgendaView(DetailView):
    model = Agenda
    template_name = "agenda_detalle.html"


 

