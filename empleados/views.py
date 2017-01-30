from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Empleado
from .forms import EmployeeForm

class EmployeeListView(View):
    template_name = "empleados.html"

    def get(self, request, *args, **kwargs):
    	empleados_activos = Empleado.objects.all()
        return render(request, self.template_name, {'empleados':empleados_activos})


class CreateEmployeeView(FormView):
    template_name = "creacion_empleados.html"
    form_class = EmployeeForm

    def get(self, request, *args, **kwargs):
    	return render(request, self.template_name)