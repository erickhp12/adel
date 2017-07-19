import os
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.http import HttpResponseRedirect
from .models import Visitas
from .forms import RegistrarVisita
from django.conf import settings

class VisitListView(ListView):
    template_name = "visitas.html"

    def get(self, request, *args, **kwargs):
        total = Visitas.objects.all().order_by('fecha_visita')
        total_visitas = Visitas.objects.all().count
        
        context = {'visitas':total,
                    'total_visitas':total_visitas,        
                    }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente = request.POST.get('visita')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final')

        if fecha_final and fecha_final != "":
            total_visitas = Visitas.objects.all().filter(fecha_visita__range=[fecha_inicial, fecha_final + " 23:59:59"])
        else:
            total_visitas = Visitas.objects.all().filter(paciente__nombres__icontains=paciente
                ) | Visitas.objects.all().filter(paciente__apellidos__icontains=paciente
                ) | Visitas.objects.all().filter(motivo__icontains=paciente)
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
        visitas = Visitas.objects.filter(id=pk)
        context = {'visitas':visitas,
                    }
        return render(request,self.template_name, context)

class DeleteVisitView(ListView):
    template_name = "eliminar_visita.html"

    def get(self, request, pk, **kwargs):
        visita = Visitas.objects.all().filter(id=pk)

        context = {'visita':visita,      
                    }
        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        Visitas.objects.all().filter(id=pk).delete()
        return render(self.request,'visitas.html')

