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
        total = Visitas.objects.all()
        total_visitas = Visitas.objects.all().count
        
        context = {'visitas':total,
                    'total_visitas':total_visitas,        
                    }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente = request.POST.get('visita')
        total_visitas = Visitas.objects.all().filter(paciente__nombres__contains=paciente
            ) | Visitas.objects.all().filter(paciente__apellidos__contains=paciente)
        total = total_visitas.count()

        context = {'visitas':total_visitas,'total_visitas':total}
        
        return render(self.request, self.template_name, context)

        
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
    template_name = "visita_detalle.html" 

    def get(self, request, pk, **kwargs):
        visitas = Visitas.objects.all().filter(id=pk)
        context = {'visitas':visitas,
                    }
        return render(request,self.template_name, context)

