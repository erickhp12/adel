from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Empleado
from .forms import RegistrarEmpleado
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class EmployeeListView(ListView):
    template_name = "empleados.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        user_logged = request.user
        empleados = Empleado.objects.filter(user=request.user)
        total_empleados = empleados.count
        mensaje = ""
        context = {'empleados': empleados,
                   'total_empleados': total_empleados,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        empleado_input = request.POST.get('empleado')
        empleados = Empleado.objects.filter(nombre__icontains=empleado_input,user=request.user
                                                  ) | Empleado.objects.filter(puesto__icontains=empleado_input,user=request.user)
        total_empleados = empleados.count()
        mensaje = ""

        if total_empleados == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = {'empleados': empleados,
                   'total_empleados': total_empleados,
                   'mensaje': mensaje,
                   }

        return render(self.request, self.template_name, context)


class CreateEmployeeView(ListView):
    template_name = "creacion_empleados.html"
    template_main = "empleados.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        empleados = Empleado.objects.filter(user=request.user)
        total_empleados = empleados.count
        mensaje = ""
        context = {'empleados': empleados,
                   'total_empleados': total_empleados,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        empleados = Empleado.objects.filter(user=request.user)
        total_empleados = empleados.count
        user = request.user
        nombre = request.POST.get('nombre')
        puesto = request.POST.get('puesto')
        edad = request.POST.get('edad')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')

        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                Empleado.objects.create(
                    user=user,
                    nombre=nombre,
                    puesto=puesto,
                    edad=edad,
                    telefono=telefono,
                    correo=correo,
                    direccion=direccion
                )
        except Exception as e:
            mensaje = "Error al crear empleado " + str(e)

        context = {'empleados': empleados,
                   'total_empleados': total_empleados,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.empleados')


class UpdateEmployeeView(ListView):
    template_name = "edicion_empleados.html"
    template_main = "empleados.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        empleado = Empleado.objects.get(user=request.user,id=pk)
        mensaje = ""
        context = {'empleado': empleado,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        empleados = Empleado.objects.filter(user=request.user)
        total_empleados = empleados.count
        user = request.user
        nombre = request.POST.get('nombre')
        puesto = request.POST.get('puesto')
        edad = request.POST.get('edad')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')

        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                empleado = Empleado.objects.get(user=request.user,id=pk)
                empleado.nombre = nombre
                empleado.puesto = puesto
                empleado.edad = edad
                empleado.telefono = telefono
                empleado.correo = correo
                empleado.direccion = direccion
                empleado.save()
        except Exception as e:
            mensaje = "Error al editar empleado " + str(e)

        context = {'empleados': empleados,
                   'total_empleados': total_empleados,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.empleados')


class DetailEmployeeView(DetailView):
    model = Empleado
    template_name = "empleado_detalle.html"


class DeleteEmployeeView(ListView):
    template_name = "eliminar_empleado.html"

    def get(self, request, pk, **kwargs):
        empleado = Empleado.objects.get(id=pk)
        context = {'empleado': empleado}

        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        mensaje = ""
        Empleado.objects.get(id=pk).delete()
        empleados = Empleado.objects.filter(user=request.user)
        total_empleados = empleados.count
        context = {'empleados': empleados,
                   'total_empleados': total_empleados,
                   'mensaje': mensaje
                   }

        return render(self.request, 'empleados.html', context)
