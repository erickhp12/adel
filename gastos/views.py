from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from .models import Gasto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from visitas.models import Visitas
from .forms import RegistrarGasto
import time


class SpendingListView(ListView):
    template_name = "gastos.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        gastos = Gasto.objects.all().order_by('fecha_gasto')
        total_gastos = Gasto.objects.all().count

        context = {'gastos':gastos,
                    'total_gastos':total_gastos,        
                    }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        gastos = request.POST.get('gasto')
        gastos = Gasto.objects.all().filter(proveedor__nombre__icontains=gastos
            ) | Gasto.objects.all().filter(proveedor__contacto__icontains=gastos)
        total_gastos = gastos.count()

        context = {'gastos':gastos,
                    'total_gastos':total_gastos,
                    }
        
        return render(self.request, self.template_name, context)

class CreateSpendingView(CreateView):
    form_class = RegistrarGasto
    template_name = "creacion_gastos.html"
    success_url = reverse_lazy('list_gastos')

class UpdateSpendingView(UpdateView):
    model = Gasto
    form_class = RegistrarGasto
    template_name = "creacion_gastos.html"
    success_url = reverse_lazy('list_gastos')	

class DeleteSpendingView(ListView):
    template_name = "eliminar_gastos.html"

    def get(self, request, pk, **kwargs):
        gastos = Gasto.objects.all().filter(id=pk)

        context = {'gastos':gastos,      
                    }
        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        Gasto.objects.all().filter(id=pk).delete()
        return render(self.request,'gastos.html')
 
class DetailSpendingView(DetailView):
    model = Gasto
    template_name = "gastos_detalle.html"


class MovementsView(ListView):
    template_name = "movimientos.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        total_diferencia = 0
        dia = time.strftime("%Y-%m-%d")
        ingresos = Visitas.objects.filter(fecha_visita__range=[dia, dia + " 23:59:59"])
        egresos = Gasto.objects.filter(fecha_gasto__range=[dia, dia + " 23:59:59"])
        ingresos_pesos = Visitas.objects.all().filter(dolares='Pesos',fecha_visita__range=[dia, dia + " 23:59:59"])
        egresos_pesos = Gasto.objects.all().filter(dolares='Pesos',fecha_gasto__range=[dia, dia + " 23:59:59"])
        ingresos_dolares = Visitas.objects.all().filter(dolares='Dolares',fecha_visita__range=[dia, dia + " 23:59:59"])
        egresos_dolares = Gasto.objects.all().filter(dolares='Dolares',fecha_gasto__range=[dia, dia + " 23:59:59"])
        
        #Calcula total de entrada de efectivo
        total_ingresos_pesos = ingresos_pesos.aggregate(Sum('precio')).get('precio__sum') 
        total_egresos_pesos = egresos_pesos.aggregate(Sum('precio')).get('precio__sum')
        total_ingresos_dolares = ingresos_dolares.aggregate(Sum('precio')).get('precio__sum')
        total_egresos_dolares = egresos_dolares.aggregate(Sum('precio')).get('precio__sum')

        #Validaciones aritmeticas
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

        context = {'ingresos':ingresos,
                    'egresos':egresos,
                    'total_ingresos_pesos':total_ingresos_pesos,
                    'total_ingresos_dolares':total_ingresos_dolares,
                    'total_egresos_pesos':total_egresos_pesos,
                    'total_egresos_dolares':total_egresos_dolares,
                    'total_diferencia_pesos': total_diferencia_pesos,
                    'total_diferencia_dolares': total_diferencia_dolares,
                    'fechai':dia,
                    'fechaf':dia,
                    }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        total_diferencia = 0
        fecha_inicio = request.POST.get('fecha1')
        fecha_final = request.POST.get('fecha2') + " 23:59:59"
        
        ingresos = Visitas.objects.filter(fecha_visita__range=[fecha_inicio, fecha_final])
        egresos = Gasto.objects.filter(fecha_gasto__range=[fecha_inicio, fecha_final])        
        ingresos_pesos = Visitas.objects.all().filter(dolares='Pesos',fecha_visita__range=[fecha_inicio, fecha_final])
        egresos_pesos = Gasto.objects.all().filter(dolares='Pesos',fecha_gasto__range=[fecha_inicio, fecha_final])
        ingresos_dolares = Visitas.objects.all().filter(dolares='Dolares',fecha_visita__range=[fecha_inicio, fecha_final])
        egresos_dolares = Gasto.objects.all().filter(dolares='Dolares',fecha_gasto__range=[fecha_inicio, fecha_final])
        
        fecha_final = request.POST.get('fecha2')
        
        total_ingresos_pesos = ingresos_pesos.aggregate(Sum('precio')).get('precio__sum') 
        total_egresos_pesos = egresos_pesos.aggregate(Sum('precio')).get('precio__sum')
        total_ingresos_dolares = ingresos_dolares.aggregate(Sum('precio')).get('precio__sum')
        total_egresos_dolares = egresos_dolares.aggregate(Sum('precio')).get('precio__sum')


        #Validaciones aritmeticas
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

        context = {'ingresos':ingresos,
                    'egresos':egresos,
                    'total_ingresos_pesos':total_ingresos_pesos,
                    'total_ingresos_dolares':total_ingresos_dolares,
                    'total_egresos_pesos':total_egresos_pesos,
                    'total_egresos_dolares':total_egresos_dolares,
                    'total_diferencia_pesos': total_diferencia_pesos,
                    'total_diferencia_dolares': total_diferencia_dolares,
                    'fechai':fecha_inicio,
                    'fechaf':fecha_final
                    }
        return render(request,self.template_name, context)
