from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Visitas
from .forms import RegistrarVisita


class VisitListView(ListView):
    queryset = Visitas.objects.all().order_by('fecha_visita')
    template_name = "visitas.html"

    def get_context_data(self, **kwargs):
        context = super(VisitListView, self).get_context_data(**kwargs)
        context['total'] = Visitas.objects.all().count()
        return context

class CreateVisitView(CreateView):
    form_class = RegistrarVisita
    template_name = "creacion_visitas.html"
    success_url = reverse_lazy('list_visitas')

class UpdateVisitView(UpdateView):
    model = Visitas
    form_class = RegistrarVisita
    template_name = "creacion_visitas.html"
    success_url = reverse_lazy('editar_visita')	
 
class DetailVisitView(DetailView):
    model = Visitas
    template_name = "visita_detalle.html"  