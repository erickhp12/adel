from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Paciente
from visitas.models import Visitas
from .forms import RegistrarPaciente
from django.http import HttpResponse


class PatientListView(ListView):
    queryset = Paciente.objects.all()
    template_name = "pacientes.html"

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)
        context['total'] = Paciente.objects.all().count()
        return context

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
        context = {'visitas':visitas,
                    'paciente':paciente,
                    }
        return render(request,self.template_name, context)

 

