from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Empleado
from .forms import RegistrarEmpleado
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class EmployeeListView(ListView):
    queryset = Empleado.objects.all().order_by('nombres')
    template_name = "empleados.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        user_logged = request.user
        empleados = Empleado.objects.filter(user=request.user)
        total_empleados = empleados.count
        mensaje = ""
        context = {'empleados':empleados,
                    'total_empleados':total_empleados,
                    'mensaje':mensaje      
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        empleado_input = request.POST.get('empleado')
        empleados = Empleado.objects.all().filter(nombre__icontains=empleado_input
            ) | Empleado.objects.all().filter(puesto__icontains=empleado_input)
        total_empleados = empleados.count()
        mensaje = ""

        if total_empleados == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = {'empleados':empleados,
                    'total_empleados':total_empleados,
                    'mensaje': mensaje,
                    }
        
        return render(self.request, self.template_name, context)


class CreateEmployeeView(CreateView):
    template_name = "creacion_empleados.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        empleados = Empleado.objects.filter(user=request.user)
        total_empleados = empleados.count
        mensaje = ""
        context = {'empleados':empleados,
                    'total_empleados':total_empleados,
                    'mensaje':mensaje      
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        # mensaje = ""
        user = request.user
        nombre = request.POST.get('nombre')
        puesto = request.POST.get('puesto')
        edad = request.POST.get('edad')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')

        print "usuario"
        print user
        print "nombre"
        print nombre
        print "estado_civil "
        print puesto
        print "edad "
        print edad
        print "telefono "
        print telefono
        print "correo"
        print correo
        print "direccion "
        print direccion

        Empleado.objects.create(
            user=user,
            nombre=nombre,
            puesto=puesto,
            edad=edad,
            telefono=telefono,
            correo=correo,
            direccion=direccion
        )

        return render(self.request, self.template_name)


class UpdateEmployeeView(UpdateView):
    model = Empleado
    form_class = RegistrarEmpleado
    template_name = "creacion_empleados.html"
    success_url = reverse_lazy('list_empleados')


class DetailEmployeeView(DetailView):
    model = Empleado
    template_name = "empleado_detalle.html"


class DeleteEmployeeView(ListView):
    template_name = "eliminar_empleado.html"

    def get(self, request, pk, **kwargs):
        empleado = Empleado.objects.all().filter(id=pk)

        context = {'empleado':empleado}

        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        Empleado.objects.all().filter(id=pk).delete()
        return render(self.request,'empleados.html')