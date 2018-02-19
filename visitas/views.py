# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.http import HttpResponseRedirect
from .models import Visitas
from .models import Paciente
from .models import Empleado
from .forms import RegistrarVisita
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class VisitListView(ListView): 
    template_name = "visitas.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        QueryVisitas = Visitas.objects.filter(user=request.user).order_by('-fecha_visita')
        total = QueryVisitas.count()
        paginator = Paginator(QueryVisitas, 50)
        page = request.GET.get('page')
        
        try:
            visitas = paginator.page(page)
        except PageNotAnInteger:
            visitas = paginator.page(1)
        except EmptyPage:
            visitas = paginator.page(paginator.num_pages)
        
        mensaje = ""

        if total == 0:
            mensaje = "No tienes visitas registradas"

        context = {
                    'visitas':visitas,
                    'total':total,
                    'mensaje': mensaje    
                    }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente = request.POST.get('visita')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final')
        mensaje = ""

        
        if fecha_final and fecha_final != "":
            visitas = Visitas.objects.all().filter(fecha_visita__range=[fecha_inicial, fecha_final + " 23:59:59"],user=request.user).order_by('-fecha_visita')
        else:
            visitas = Visitas.objects.all().filter(paciente__nombre__icontains=paciente,user=request.user
                ) | Visitas.objects.all().filter(motivo__icontains=paciente,user=request.user).order_by('-fecha_visita')
        total = visitas.count()

        if visitas == 0:
            mensaje = "No tienes visitas en estas fechas"

        context = {'visitas':visitas,
                    'total':total,
                    'mensaje': mensaje    
                    }
        
        return render(self.request, self.template_name, context)


        
class CreateVisitView(ListView):
    template_name = "visitas-formulario.html"
    template_main = "visitas.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        pacientes = Paciente.objects.filter(user=request.user).order_by('nombre')
        empleados = Empleado.objects.filter(user=request.user).order_by('nombre')

        form = RegistrarVisita()
        mensaje = ""
        context = {'pacientes': pacientes,
                    'empleados':empleados,
                    'form':form,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        visitas = Visitas.objects.filter(user=request.user)
        total = visitas.count
        user = request.user
        pacienteSeleccionado = request.POST.get('paciente')
        paciente = Paciente.objects.filter(nombre=pacienteSeleccionado).first()
        motivo = request.POST.get('motivo')
        empleadoSeleccionado = request.POST.get('empleado')
        empleado = Empleado.objects.filter(nombre=empleadoSeleccionado).first()
        precio = request.POST.get('precio')
        dolares = request.POST.get('dolares')
        tipo_pago = request.POST.get('tipo_pago')
        fecha_visita = request.POST.get('fecha') 


        try:
            if paciente == "":
                return render(self.request, self.template_name)
            else:
                Visitas.objects.create(
                    user=user,
                    paciente=paciente,
                    motivo=motivo,
                    dentista=empleado,
                    precio=precio,
                    dolares=dolares,
                    tipo_pago=tipo_pago,
                    fecha_visita=fecha_visita
                )
        except Exception as e:
            mensaje = "Error al crear visita " + str(e)

        context = {'visitas': visitas,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.visitas')


class UpdateVisitView(ListView):
    template_name = "visitas-formulario.html"
    template_main = "visitas.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        visita = Visitas.objects.get(user=request.user,id=pk)
        pacientes = Paciente.objects.filter(user=request.user)
        empleados = Empleado.objects.filter(user=request.user)
        form = RegistrarVisita()
        mensaje = ""


        context = {
                    'visita': visita,
                    'mensaje': mensaje,
                    'pacientes':pacientes,
                    'form':form,
                    'empleados':empleados
                   }

        return render(request, self.template_name, context)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        visitas = Visitas.objects.filter(user=request.user)
        total = visitas.count
        user = request.user
        pacienteSeleccionado = request.POST.get('paciente')
        paciente = Paciente.objects.filter(nombre=pacienteSeleccionado).first()
        motivo = request.POST.get('motivo')
        empleadoSeleccionado = request.POST.get('empleado')
        empleado = Empleado.objects.filter(nombre=empleadoSeleccionado).first()
        precio = request.POST.get('precio')
        dolares = request.POST.get('dolares')
        tipo_pago = request.POST.get('tipo_pago')
        fecha_visita = request.POST.get('fecha')


        try:
            if paciente == "":
                return render(self.request, self.template_name)
            else:
                visita = Visitas.objects.get(user=request.user,id=pk)
                visita.paciente = paciente
                visita.motivo = motivo
                visita.empleado = empleado
                visita.precio = precio
                visita.dolares = dolares
                visita.tipo_pago = tipo_pago
                visita.fecha_visita = fecha_visita
                visita.save()
        except Exception as e:
            mensaje = "Error al editar visita " + str(e)

        context = {'visitas': visitas,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.visitas')	


class DeleteVisitView(ListView):
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):

        Visitas.objects.filter(id=pk,user=request.user).delete()

        return render(request,'visitas.html')

