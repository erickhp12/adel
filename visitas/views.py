from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from .models import Visitas
from .forms import RegistrarVisita


class VisitListView(ListView):
    queryset = Visitas.objects.all().order_by('fecha_visita')
    template_name = "visitas.html"

    def get(self, request, *args, **kwargs):
        visitas = Visitas.objects.all()
        total_visitas = Visitas.objects.all().count
        total_pesos = Visitas.objects.filter(precio__isnull=False,dolares='pesos').aggregate(Sum('precio'))
        total_dolares = Visitas.objects.filter(precio__isnull=False,dolares='dolares').aggregate(Sum('precio'))

        context = {'visitas':visitas,
                    'total_visitas':total_visitas,
                    'total_pesos':total_pesos,
                    'total_dolares':total_dolares,
                    }
        return render(request,self.template_name, context)

class CreateVisitView(CreateView):
    form_class = RegistrarVisita
    template_name = "creacion_visitas.html"
    success_url = reverse_lazy('list_visitas')

class UpdateVisitView(UpdateView):
    model = Visitas
    form_class = RegistrarVisita
    template_name = "creacion_visitas.html"
    success_url = reverse_lazy('list_visitas')	
 
class DetailVisitView(DetailView):
    model = Visitas
    template_name = "visita_detalle.html"  