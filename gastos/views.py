from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from proveedores.models import Proveedor
from empleados.models import Empleado
from visitas.models import Visitas
from .models import Gasto
from .forms import RegistrarGasto
from . import forms
import time


class SpendingListView(ListView):
    template_name = "gastos.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        gastos = Gasto.objects.filter(user=request.user).order_by('-fecha_gasto')
        total = gastos.count()
        mensaje = ""
        
        if total == 0:
            mensaje = "No tienes gastos registrados"

        context = {'gastos': gastos,
                   'total': total,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        gastos = request.POST.get('gasto')
        fecha_inicial = request.POST.get('fecha_inicial')
        fecha_final = request.POST.get('fecha_final')
        mensaje = ""
        
        if fecha_final and fecha_final != "":
            gastos = Gasto.objects.filter(
                fecha_gasto__range=[fecha_inicial, fecha_final + " 23:59:59"],user=request.user)
        else:
            gastos = Gasto.objects.filter(proveedor__nombre__icontains=gastos,user=request.user
                ) | Gasto.objects.filter(proveedor__contacto__icontains=gastos,user=request.user
                ) | Gasto.objects.filter(motivo__icontains=gastos,user=request.user).order_by('-fecha_gasto')
        
        total = gastos.count()

        if total == 0:
            mensaje = "La busqueda no mostro ningun resultado"
        
        context = {'gastos': gastos,
                   'total': total,
                   'mensaje': mensaje
                   }

        return render(self.request, self.template_name, context)

class CreateSpendingView(ListView):
    template_name = "gastos-formulario.html"
    template_main = "gastos.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        proveedores = Proveedor.objects.filter(user=request.user)
        empleados = Empleado.objects.filter(user=request.user)
        form = RegistrarGasto()
        mensaje = ""
        
        context = {'proveedores': proveedores,
                    'empleados':empleados,
                    'form':form,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        gastos = Gasto.objects.filter(user=request.user)
        total = gastos.count
        user = request.user
        proveedorSeleccionado = request.POST.get('proveedor')
        proveedor = Proveedor.objects.filter(nombre=proveedorSeleccionado).first()
        motivo = request.POST.get('motivo')
        empleadoSeleccionado = request.POST.get('empleado')
        empleado = Empleado.objects.filter(nombre=empleadoSeleccionado).first()
        precio = request.POST.get('precio')
        dolares = request.POST.get('dolares')
        tipo_pago = request.POST.get('tipo_pago')
        fecha_gasto = request.POST.get('fecha') 

        try:
            if proveedor == "":
                return render(self.request, self.template_name)
            else:
                Gasto.objects.create(
                    user=user,
                    proveedor=proveedor,
                    motivo=motivo,
                    empleado=empleado,
                    precio=precio,
                    dolares=dolares,
                    tipo_pago=tipo_pago,
                    fecha_gasto=fecha_gasto
                )
        except Exception as e:
            mensaje = "Error al crear empleado " + str(e)

        context = {'gastos': gastos,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.gastos')


class UpdateSpendingView(ListView):
    template_name = "gastos-formulario.html"
    template_main = "gastos.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        gasto = Gasto.objects.get(user=request.user,id=pk)
        proveedores = Proveedor.objects.filter(user=request.user)
        empleados = Empleado.objects.filter(user=request.user)
        form = RegistrarGasto()

        mensaje = ""
        context = {'gasto': gasto,
                   'mensaje': mensaje,
                   'proveedores':proveedores,
                   'form':form,
                   'empleados':empleados
                   }

        return render(request, self.template_name, context)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        gastos = Gasto.objects.filter(user=request.user)
        total = gastos.count
        user = request.user
        proveedorSeleccionado = request.POST.get('proveedor')
        proveedor = Proveedor.objects.filter(nombre=proveedorSeleccionado).first()
        motivo = request.POST.get('motivo')
        empleadoSeleccionado = request.POST.get('empleado')
        empleado = Empleado.objects.filter(nombre=empleadoSeleccionado).first()
        precio = request.POST.get('precio')
        dolares = request.POST.get('dolares')
        tipo_pago = request.POST.get('tipo_pago')
        fecha_gasto = request.POST.get('fecha')

        print "---------------------Edicion de gasto ---------------------"
        print "user"
        print user
        print "proveedor"
        print proveedor
        print "empleado"
        print empleado
        print "precio"
        print precio
        print "dolares"
        print dolares
        print "tipo_pago"
        print tipo_pago
        print "fecha_gasto"
        print fecha_gasto


        try:
            if proveedor == "":
                return render(self.request, self.template_name)
            else:
                gasto = Gasto.objects.get(user=request.user,id=pk)
                gasto.proveedor = proveedor
                gasto.motivo = motivo
                gasto.empleado = empleado
                gasto.precio = precio
                gasto.dolares = dolares
                gasto.tipo_pago = tipo_pago
                gasto.fecha_gasto = fecha_gasto
                gasto.save()
        except Exception as e:
            print "ALGO SALIO MAL " + str(e)
            mensaje = "Error al editar gasto " + str(e)

        context = {'gastos': gastos,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.gastos')

class DeleteSpendingView(ListView):
    template_name = "eliminar_gastos.html"

    def get(self, request, pk, **kwargs):
        gasto = Gasto.objects.get(user=request.user,id=pk)

        print "BORRAR GASTO"
        print gasto.motivo
        context = {'gasto': gasto,
                   }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        gasto = Gasto.objects.get(user=request.user,id=pk)
        gastos = Gasto.objects.filter(user=request.user).order_by('fecha_gasto')
        total = gastos.count
        mensaje = ""

        Gasto.objects.get(id=pk).delete()

        context = {'gasto': gasto,
                    'gastos':gastos,
                   'total': total,
                   'mensaje': mensaje
                   }

        return render(self.request, 'gastos.html', context)


class MovementsView(ListView):
    template_name = "movimientos.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        total_diferencia = 0
        dia = time.strftime("%Y-%m-%d")
        mensaje = ""
        ingresos = Visitas.objects.filter(fecha_visita__range=[dia, dia + " 23:59:59"],user=request.user).order_by('-fecha_visita')
        egresos = Gasto.objects.filter(fecha_gasto__range=[dia, dia + " 23:59:59"],user=request.user).order_by('-fecha_gasto')
        ingresos_pesos = Visitas.objects.filter(dolares='Pesos', fecha_visita__range=[dia, dia + " 23:59:59"],user=request.user)
        egresos_pesos = Gasto.objects.filter(dolares='Pesos', fecha_gasto__range=[dia, dia + " 23:59:59"],user=request.user)
        ingresos_dolares = Visitas.objects.filter(dolares='Dolares', fecha_visita__range=[dia, dia + " 23:59:59"],user=request.user)
        egresos_dolares = Gasto.objects.filter(dolares='Dolares', fecha_gasto__range=[dia, dia + " 23:59:59"],user=request.user)

        #Calcula el total de ingresos y egresos
        total_ingresos = ingresos.count()
        total_egresos  = egresos.count()
        total = total_ingresos + total_egresos

        # Calcula total de entrada de efectivo
        total_ingresos_pesos = ingresos_pesos.aggregate(Sum('precio')).get('precio__sum')
        total_egresos_pesos = egresos_pesos.aggregate(Sum('precio')).get('precio__sum')
        total_ingresos_dolares = ingresos_dolares.aggregate(Sum('precio')).get('precio__sum')
        total_egresos_dolares = egresos_dolares.aggregate(Sum('precio')).get('precio__sum')

        if len(ingresos) == 0 and len(egresos) == 0:
            mensaje = "No tienes movimientos en el rango de fechas seleccionado"
        
        # Validaciones aritmeticas
        if total_ingresos_pesos is None:
            total_ingresos_pesos = 0
        if total_ingresos_dolares is None:
            total_ingresos_dolares = 0
        if total_egresos_pesos is None:
            total_egresos_pesos = 0
        if total_egresos_dolares is None:
            total_egresos_dolares = 0

        total_diferencia_pesos = (total_ingresos_pesos - total_egresos_pesos)
        total_diferencia_dolares = (total_ingresos_dolares - total_egresos_dolares)

        context = {
                    'total':total,
                    'ingresos': ingresos,
                    'egresos': egresos,
                    'total_ingresos': total_ingresos,
                    'total_egresos': total_egresos,
                    'total_ingresos_pesos': total_ingresos_pesos,
                    'total_ingresos_dolares': total_ingresos_dolares,
                    'total_egresos_pesos': total_egresos_pesos,
                    'total_egresos_dolares': total_egresos_dolares,
                    'total_diferencia_pesos': total_diferencia_pesos,
                    'total_diferencia_dolares': total_diferencia_dolares,
                    'fechai': dia,
                    'fechaf': dia,
                    'mensaje': mensaje,
                   }
                   
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        total_diferencia = 0
        fecha_inicio = request.POST.get('fecha1')
        fecha_final = request.POST.get('fecha2') + " 23:59:59"
        mensaje = ""
        ingresos = Visitas.objects.filter(fecha_visita__range=[fecha_inicio, fecha_final],user=request.user).order_by('-fecha_visita')
        egresos = Gasto.objects.filter(fecha_gasto__range=[fecha_inicio, fecha_final],user=request.user).order_by('-fecha_gasto')
        ingresos_pesos = Visitas.objects.all().filter(dolares='Pesos', fecha_visita__range=[fecha_inicio, fecha_final],user=request.user)
        egresos_pesos = Gasto.objects.all().filter(dolares='Pesos', fecha_gasto__range=[fecha_inicio, fecha_final],user=request.user)
        ingresos_dolares = Visitas.objects.all().filter(dolares='Dolares', fecha_visita__range=[fecha_inicio, fecha_final],user=request.user)
        egresos_dolares = Gasto.objects.all().filter(dolares='Dolares', fecha_gasto__range=[fecha_inicio, fecha_final],user=request.user)

        fecha_final = request.POST.get('fecha2')

        #Calcula el total de ingresos y egresos
        total_ingresos = ingresos.count()
        total_egresos  = egresos.count()
        total = total_ingresos + total_egresos

        # Calcula total de entrada de efectivo
        total_ingresos_pesos = ingresos_pesos.aggregate(Sum('precio')).get('precio__sum')
        total_egresos_pesos = egresos_pesos.aggregate(Sum('precio')).get('precio__sum')
        total_ingresos_dolares = ingresos_dolares.aggregate(Sum('precio')).get('precio__sum')
        total_egresos_dolares = egresos_dolares.aggregate(Sum('precio')).get('precio__sum')

        if len(ingresos) == 0 and len(egresos) == 0:
            mensaje = "No tienes movimientos en el rango de fechas seleccionado"

        # Validaciones aritmeticas
        if total_ingresos_pesos is None:
            total_ingresos_pesos = 0
        if total_ingresos_dolares is None:
            total_ingresos_dolares = 0
        if total_egresos_pesos is None:
            total_egresos_pesos = 0
        if total_egresos_dolares is None:
            total_egresos_dolares = 0

        total_diferencia_pesos = (total_ingresos_pesos - total_egresos_pesos)
        total_diferencia_dolares = (
            total_ingresos_dolares - total_egresos_dolares)

        context = {
                    'total':total,
                    'ingresos': ingresos,
                    'egresos': egresos,
                    'total_ingresos': total_ingresos,
                    'total_egresos': total_egresos,
                    'total_ingresos_pesos': total_ingresos_pesos,
                    'total_ingresos_dolares': total_ingresos_dolares,
                    'total_egresos_pesos': total_egresos_pesos,
                    'total_egresos_dolares': total_egresos_dolares,
                    'total_diferencia_pesos': total_diferencia_pesos,
                    'total_diferencia_dolares': total_diferencia_dolares,
                    'fechai': fecha_inicio,
                    'fechaf': fecha_final,
                    'mensaje': mensaje,
                   }
        return render(request, self.template_name, context)