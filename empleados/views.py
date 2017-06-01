from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Empleado
from .forms import RegistrarEmpleado


class EmployeeListView(ListView):
    queryset = Empleado.objects.all().order_by('nombres')
    template_name = "empleados.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['total'] = Empleado.objects.all().count()
        return context

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