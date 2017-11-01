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


class VisitListView(ListView): 
    template_name = "visitas.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        visitas = Visitas.objects.filter(user=request.user).order_by('fecha_visita')
        total_visitas = visitas.count()
        mensaje = ""

        if total_visitas == 0:
            mensaje = "No tienes visitas registradas"

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
            total_visitas = Visitas.objects.all().filter(fecha_visita__range=[fecha_inicial, fecha_final + " 23:59:59"],user=request.user)
        else:
            total_visitas = Visitas.objects.all().filter(paciente__nombre__icontains=paciente,user=request.user
                ) | Visitas.objects.all().filter(motivo__icontains=paciente,user=request.user)
        total = total_visitas.count()

        if total == 0:
            mensaje = "No tienes visitas en estas fechas"

        context = {'visitas':total_visitas,'total_visitas':total,'mensaje':mensaje}
        
        return render(self.request, self.template_name, context)

        
class CreateVisitView(ListView):
    template_name = "creacion_visitas.html"
    template_main = "visitas.html"

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
        visitas = Visitas.objects.filter(user=request.user)
        total_visitas = visitas.count
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
                   'total_visitas': total_visitas,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.visitas')


class UpdateVisitView(ListView):
    template_name = "edicion_visitas.html"
    template_main = "visitas.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        visita = Visitas.objects.get(user=request.user,id=pk)
        pacientes = Paciente.objects.filter(user=request.user)
        empleados = Empleado.objects.filter(user=request.user)
        form = RegistrarVisita()
        mensaje = ""

        context = {'visita': visita,
                   'mensaje': mensaje,
                   'pacientes':pacientes,
                   'form':form,
                   'empleados':empleados
                   }

        return render(request, self.template_name, context)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        visitas = Visitas.objects.filter(user=request.user)
        total_visitas = visitas.count
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

        # print "---------------------Edicion de visita ---------------------"
        # print "user"
        # print user
        # print "paciente"
        # print paciente
        # print "empleado"
        # print empleado
        # print "precio"
        # print precio
        # print "dolares"
        # print dolares
        # print "tipo_pago"
        # print tipo_pago
        # print "fecha_visita"
        # print fecha_visita


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
                   'total_visitas': total_visitas,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.visitas')	


class DeleteVisitView(ListView):
    template_name = "eliminar_visita.html"

    def get(self, request, pk, **kwargs):
        visita = Visitas.objects.all().filter(id=pk)

        context = {'visita':visita,      
                    }
        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        visitas = Visitas.objects.all().order_by('fecha_visita')
        total_visitas = visitas.count
        mensaje = ""
        Visitas.objects.all().filter(id=pk).delete()
        context = {'visitas':visitas,
                    'total_visitas':total_visitas,
                    'mensaje': mensaje    
                    }
        return render(self.request,'visitas.html',context)

