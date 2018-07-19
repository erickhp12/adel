from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Empleado
from .forms import RegistrarEmpleado
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

class EmployeeListView(ListView):
    template_name = "empleados.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        QueryEmpleados = Empleado.objects.filter(user=request.user).order_by('-fecha_inicio')
        total = QueryEmpleados.count()
        paginator = Paginator(QueryEmpleados, 50)
        page = request.GET.get('page')
        mensaje = ""
        
        try:
            empleados = paginator.page(page)
        except PageNotAnInteger:
            empleados = paginator.page(1)
        except EmptyPage:
            empleados = paginator.page(paginator.num_pages)

        if total == 0:
            mensaje = "No tienes empleados registrados"

        context = {
                    'empleados': empleados,
                    'total': total,
                    'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        empleado_input = request.POST.get('empleado')
        empleados = Empleado.objects.filter(nombre__icontains=empleado_input,user=request.user
                    ) | Empleado.objects.filter(puesto__icontains=empleado_input,user=request.user).order_by('-fecha_inicio')
        total = empleados.count()
        mensaje = ""

        if total == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = { 
                    'empleados': empleados,
                    'total': total,
                    'mensaje': mensaje,
                   }

        return render(self.request, self.template_name, context)


class CreateEmployeeView(ListView):
    template_name = "empleados-formulario.html"
    template_main = "empleados.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        empleados = Empleado.objects.filter(user=request.user)
        total = empleados.count
        now = datetime.datetime.now()
        currentYear = now.year
        years = []
        year = 1920

        while currentYear >= year:
            years.append(currentYear)
            currentYear-=1

        mensaje = ""
        context = {
                    'empleados': empleados,
                    'years':years,
                    'total': total,
                    'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        empleados = Empleado.objects.filter(user=request.user)
        total = empleados.count
        user = request.user
        nombre = request.POST.get('nombre')
        puesto = request.POST.get('puesto')
        usuarioDay = request.POST.get('day')
        usuarioMonth = request.POST.get('month')
        usuarioYear = request.POST.get('year')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        birth = usuarioYear + "-" + usuarioMonth + "-" + usuarioDay

        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                Empleado.objects.create(
                    user=user,
                    nombre=nombre,
                    puesto=puesto,
                    fecha_nacimiento=birth,
                    telefono=telefono,
                    correo=correo,
                    direccion=direccion
                )
        except Exception as e:
            print "ERROR "
            print str(e)
            mensaje = "Error al crear empleado " + str(e)

        context = {
                    'empleados': empleados,
                    'total': total,
                    'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.empleados')


class UpdateEmployeeView(ListView):
    template_name = "empleados-formulario.html"
    template_main = "empleados.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        empleado = Empleado.objects.get(user=request.user,id=pk)
        now = datetime.datetime.now()
        currentYear = now.year
        years = []
        year = 1920
        usuarioDia = ""
        usuarioMes = ""
        usuarioYear = ""

        if empleado.fecha_nacimiento != None:
            fecha = empleado.fecha_nacimiento.strftime('%m/%d/%Y')
            usuarioMes = fecha[0:2]
            usuarioDia =  fecha[3:5]
            usuarioYear = fecha[6:10]

        while currentYear >= year:
            years.append(currentYear)
            currentYear-=1
        mensaje = ""

        context = {
                    'empleado': empleado,
                    'usuarioDia':usuarioDia,
                    'usuarioMes':usuarioMes,
                    'usuarioYear':usuarioYear,
                    'years':years,
                    'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        empleados = Empleado.objects.filter(user=request.user)
        total = empleados.count
        user = request.user
        nombre = request.POST.get('nombre')
        puesto = request.POST.get('puesto')
        usuarioDay = request.POST.get('day')
        usuarioMonth = request.POST.get('month')
        usuarioYear = request.POST.get('year')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        
        birth = usuarioYear + "-" + usuarioMonth + "-" + usuarioDay
        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                empleado = Empleado.objects.get(user=request.user,id=pk)
                empleado.nombre = nombre
                empleado.puesto = puesto
                empleado.fecha_nacimiento = birth
                empleado.telefono = telefono
                empleado.correo = correo
                empleado.direccion = direccion
                empleado.save()
        except Exception as e:
            mensaje = "Error al editar empleado " + str(e)

        context = {
                    'empleados': empleados,
                    'total': total,
                    'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.empleados')



class DeleteEmployeeView(ListView):
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):
        Empleado.objects.filter(id=pk,user=request.user).delete()

        return render(request,'empleados.html')
