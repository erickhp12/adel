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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator


class ReceiptListView(ListView): 
    template_name = "recetas.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        QueryRecetas = Recetas.objects.filter(user=request.user).order_by('-fecha_receta')
        total = QueryRecetas.count()
        paginator = Paginator(QueryRecetas, 50)
        page = request.GET.get('page')
        mensaje = ""
        
        try:
            recetas = paginator.page(page)
        except PageNotAnInteger:
            recetas = paginator.page(1)
        except EmptyPage:
            recetas = paginator.page(paginator.num_pages)


        if total == 0:
            mensaje = "No tienes Recetas registradas"

        context = {
                    'recetas':recetas,
                    'total':total,
                    'mensaje': mensaje    
                    }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente = request.POST.get('receta')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final')
        mensaje = ""

        if fecha_final and fecha_final != "":
            recetas = Recetas.objects.all().filter(fecha_receta__range=[fecha_inicial, fecha_final + " 23:59:59"],user=request.user).order_by('-fecha_receta')
        else:
            recetas = Recetas.objects.filter(paciente__nombre__icontains=paciente,user=request.user
                ) | Recetas.objects.all().filter(comentario__icontains=paciente,user=request.user).order_by('-fecha_receta')
        total = recetas.count

        if recetas == 0:
            mensaje = "No tienes recetas en estas fechas"

        context = {'recetas':recetas,
                    'total':total,
                    'mensaje': mensaje    
                    }
        
        return render(self.request, self.template_name, context)


        
class CreateReceiptView(ListView):
    template_name = "recetas-formulario.html"
    template_main = "recetas.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        pacientes = Paciente.objects.filter(user=request.user).order_by('nombre')
        empleados = Empleado.objects.filter(user=request.user).order_by('nombre')
        form = RegistrarReceta()
        mensaje = ""
        context = {'pacientes': pacientes,
                    'empleados':empleados,
                    'form':form,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        recetas = Recetas.objects.filter(user=request.user)
        total = recetas.count
        user = request.user
        pacienteSeleccionado = request.POST.get('paciente')
        paciente = Paciente.objects.filter(nombre=pacienteSeleccionado).first()
        motivo = request.POST.get('motivo')
        comentario = request.POST.get('comentario')
        empleadoSeleccionado = request.POST.get('empleado')
        empleado = Empleado.objects.filter(nombre=empleadoSeleccionado).first()
        fecha_receta = request.POST.get('fecha') 


        try:
            if paciente == "":
                return render(self.request, self.template_name)
            else:
                Recetas.objects.create(
                    user=user,
                    paciente=paciente,
                    motivo=motivo,
                    comentario=comentario,
                    dentista=empleado,
                    fecha_receta=fecha_receta
                )
        except Exception as e:
            mensaje = "Error al crear receta " + str(e)

        context = {'Recetas': Recetas,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.recetas')


class UpdateReceiptView(ListView):
    template_name = "recetas-formulario.html"
    template_main = "recetas.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        receta = Recetas.objects.get(user=request.user,id=pk)
        pacientes = Paciente.objects.filter(user=request.user).order_by('nombre')
        empleados = Empleado.objects.filter(user=request.user).order_by('nombre')
        form = RegistrarReceta()
        mensaje = ""


        context = {
                    'receta': receta,
                    'mensaje': mensaje,
                    'pacientes':pacientes,
                    'form':form,
                    'empleados':empleados
                   }

        return render(request, self.template_name, context)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        recetas = Recetas.objects.filter(user=request.user)
        total = recetas.count
        user = request.user
        pacienteSeleccionado = request.POST.get('paciente')
        paciente = Paciente.objects.filter(nombre=pacienteSeleccionado).first()
        motivo = request.POST.get('motivo')
        comentario = request.POST.get('comentario')
        empleadoSeleccionado = request.POST.get('empleado')
        empleado = Empleado.objects.filter(nombre=empleadoSeleccionado).first()
        fecha_receta = request.POST.get('fecha')

        try:
            if paciente == "":
                return render(self.request, self.template_name)
            else:
                receta = Recetas.objects.get(user=request.user,id=pk)
                receta.paciente = paciente
                receta.motivo = motivo
                receta.comentario = comentario
                receta.empleado = empleado
                receta.fecha_receta = fecha_receta
                receta.save()
        except Exception as e:
            mensaje = "Error al editar receta " + str(e)

        context = {'recetas': recetas,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.recetas')	

class DeleteReceiptView(ListView):
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):
        Recetas.objects.filter(id=pk,user=request.user).delete()

        return render(request,'recetas.html')