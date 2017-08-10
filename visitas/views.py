# -*- coding: utf-8 -*-
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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class VisitListView(ListView):
    template_name = "visitas.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        visitas = Visitas.objects.all().order_by('fecha_visita')
        total_visitas = visitas.count
        mensaje = ""
        context = {'visitas':visitas,
                    'total_visitas':total_visitas,
                    'mensaje': mensaje    
                    }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente = request.POST.get('visita')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final')
        mensaje = ""

        
        if fecha_final and fecha_final != "":
            total_visitas = Visitas.objects.all().filter(fecha_visita__range=[fecha_inicial, fecha_final + " 23:59:59"])
        else:
            total_visitas = Visitas.objects.all().filter(paciente__nombre__icontains=paciente
                ) | Visitas.objects.all().filter(motivo__icontains=paciente)
        total = total_visitas.count()

        if total == 0:
            mensaje = "No tienes visitas en estas fechas"

        context = {'visitas':total_visitas,'total_visitas':total,'mensaje':mensaje}
        
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

