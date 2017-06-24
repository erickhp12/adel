from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from .models import Gasto 
from visitas.models import Visitas
from .forms import RegistrarGasto
import time


class SpendingListView(ListView):
    template_name = "gastos.html"

    def get(self, request, *args, **kwargs):
        gastos = Gasto.objects.all().order_by('fecha_gasto')
        total_gastos = Gasto.objects.all().count
        
        context = {'gastos':gastos,
                    'total_gastos':total_gastos,        
                    }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        gastos = request.POST.get('gasto')
        gastos = Gasto.objects.all().filter(proveedor__nombre__contains=gastos
            ) | Gasto.objects.all().filter(proveedor__contacto__contains=gastos)
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
 
class DetailSpendingView(DetailView):
    model = Gasto
    template_name = "gastos_detalle.html"  


class MovementsView(ListView):
    template_name = "movimientos.html"

    def get(self, request, *args, **kwargs):
        total_diferencia = 0
        dia = time.strftime("%Y-%m-%d")
        ingresos = Visitas.objects.filter(fecha_visita__range=[dia, dia + " 23:59:59"])
        egresos = Gasto.objects.filter(fecha_gasto__range=[dia, dia + " 23:59:59"])
        total_ingresos = ingresos.aggregate(Sum('precio')).get('precio__sum') 
        total_egresos = egresos.aggregate(Sum('precio')).get('precio__sum')
 
        if total_ingresos is not None and total_egresos is not None: 
            total_diferencia = (total_ingresos - total_egresos) 
        elif total_ingresos is None:
            total_ingresos = 0
        if total_egresos is None:
            total_egresos = 0
            total_diferencia = total_ingresos

        context = {'ingresos':ingresos,
                    'egresos':egresos,
                    'total_ingresos':total_ingresos,
                    'total_egresos':total_egresos,
                    'total_diferencia':total_diferencia,
                    'fechai':dia,
                    'fechaf':dia,
                    }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        fecha_inicio = request.POST.get('fecha1')
        fecha_final = request.POST.get('fecha2') + " 23:59:59"
        
        ingresos = Visitas.objects.filter(fecha_visita__range=[fecha_inicio, fecha_final])
        egresos = Gasto.objects.filter(fecha_gasto__range=[fecha_inicio, fecha_final])
        total_ingresos = ingresos.aggregate(Sum('precio')).get('precio__sum') 
        total_egresos = egresos.aggregate(Sum('precio')).get('precio__sum')
        total_diferencia = 0
        fecha_final = request.POST.get('fecha2')
        
        if total_ingresos is not None and total_egresos is not None: 
            total_diferencia = (total_ingresos - total_egresos) 
        elif total_ingresos is None:
            total_ingresos = 0
        if total_egresos is None:
            total_egresos = 0
            total_diferencia = total_ingresos
         
        context = {'ingresos':ingresos,
                    'egresos':egresos,
                    'total_ingresos':total_ingresos,
                    'total_egresos':total_egresos,
                    'total_diferencia': total_diferencia,
                    'fechai':fecha_inicio,
                    'fechaf':fecha_final
                    }
        return render(request,self.template_name, context)
