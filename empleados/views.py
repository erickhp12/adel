from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Empleado
from .forms import RegistrarEmpleado


class EmployeeListView(ListView):
    queryset = Empleado.objects.all()
    template_name = "empleados.html"

class CreateEmployeeView(CreateView):
    form_class = RegistrarEmpleado
    template_name = "creacion_empleados.html"
    success_url = reverse_lazy('list_empleados')

class UpdateEmployeeView(UpdateView):
    model = Empleado
    form_class = RegistrarEmpleado
    template_name = "creacion_empleados.html"
    success_url = reverse_lazy('list_empleados')	


class DetailEmployeeView(DetailView):
    model = Empleado
    template_name = "empleado_detalle.html"