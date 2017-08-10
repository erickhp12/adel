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
        empleados = Empleado.objects.all()
        total_empleados = Empleado.objects.all().count
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


class DeleteEmployeeView(ListView):
    template_name = "eliminar_empleado.html"

    def get(self, request, pk, **kwargs):
        empleado = Empleado.objects.all().filter(id=pk)

        context = {'empleado':empleado}

        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        Empleado.objects.all().filter(id=pk).delete()
        return render(self.request,'empleados.html')