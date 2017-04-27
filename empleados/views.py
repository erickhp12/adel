from django.shortcuts import render
from django.views.generic import View, FormView
from .models import Empleado
from .forms import RegistrarEmpleado


class EmployeeListView(View):
    template_name = "empleados.html"

    def get(self, request, *args, **kwargs):
        empleados_activos = Empleado.objects.all()
        return render(request, self.template_name, {
            'empleados': empleados_activos,
            'message': 'Aqui andamos'
        })


class CreateEmployeeView(FormView):
    template_name = "creacion_empleados.html"
    message = "Aqui andamos al cien"

    def get(self, request, *args, **kwargs):
        form = RegistrarEmpleado()
        data = {
            'form': form
        }
        return render(request,  self.template_name,  data)

    def post(self, request, *args, **kwargs):
        form = RegistrarEmpleado(request.POST)
        data = {
            'form': form,
        }
        if form.is_valid():
            form.save(commit=True)
            message = "Agregado correctamente"
            data = {
                'form': form,
                'message': message
            }
            return render(request, self.template_name, data)
        else:
            message = "algo no es valido"
            data = {
                'form': form,
                'message': message,
            }
            return render(request, self.template_name, data)
