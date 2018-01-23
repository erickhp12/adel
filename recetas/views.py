# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.http import HttpResponseRedirect
from .models import Recetas
from .models import Paciente
from .models import Empleado
from .forms import RegistrarReceta
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ReceiptListView(ListView): 
    template_name = "recetas.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        recetas = Recetas.objects.filter(user=request.user).order_by('-fecha_receta')
        total = recetas.count()
        mensaje = ""

        if total == 0:
            mensaje = "No tienes Recetas registradas"

        context = {'recetas':recetas,
                    'total':total,
                    'mensaje': mensaje    
                    }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente = request.POST.get('visita')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final')
        mensaje = ""

        print "2018 visita"
        print paciente

        
        if fecha_final and fecha_final != "":
            Recetas = Recetas.objects.all().filter(fecha_visita__range=[fecha_inicial, fecha_final + " 23:59:59"],user=request.user).order_by('-fecha_visita')
        else:
            Recetas = Recetas.objects.all().filter(paciente__nombre__icontains=paciente,user=request.user
                ) | Recetas.objects.all().filter(motivo__icontains=paciente,user=request.user).order_by('-fecha_visita')
        total = Recetas.count()

        if Recetas == 0:
            mensaje = "No tienes Recetas en estas fechas"

        context = {'Recetas':Recetas,
                    'total':total,
                    'mensaje': mensaje    
                    }
        
        return render(self.request, self.template_name, context)


        
class CreateReceiptView(ListView):
    template_name = "Recetas-formulario.html"
    template_main = "Recetas.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        pacientes = Paciente.objects.filter(user=request.user)
        empleados = Empleado.objects.filter(user=request.user)
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
        Recetas = Recetas.objects.filter(user=request.user)
        total = Recetas.count
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

        # print "user ", user
        # print "paciente ", paciente
        # print "motivo ", motivo
        # print "empleado ", empleado
        # print "precio ", precio
        # print "dolares ", dolares
        # print "tipo_pago ", tipo_pago
        # print "fecha_visita ", fecha_visita

        try:
            if paciente == "":
                return render(self.request, self.template_name)
            else:
                Recetas.objects.create(
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

        context = {'Recetas': Recetas,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.Recetas')
