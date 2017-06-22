from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Empleado
from .forms import RegistrarEmpleado


class EmployeeListView(ListView):
    queryset = Empleado.objects.all().order_by('nombres')
    template_name = "empleados.html"

    def get(self, request, *args, **kwargs):
        empleados = Empleado.objects.all()
        total_empleados = Empleado.objects.all().count
        
        context = {'empleados':empleados,
                    'total_empleados':total_empleados,        
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        empleado_input = request.POST.get('empleado')

        empleados = Empleado.objects.all().filter(nombres__contains=empleado_input
            ) | Empleado.objects.all().filter(apellidos__contains=empleado_input)
        total_empleados = empleados.count()

        context = {'empleados':empleados,
                    'total_empleados':total_empleados
                    }
        
        return render(self.request, self.template_name, context)

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