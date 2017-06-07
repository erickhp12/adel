from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from .models import Gasto
from .forms import RegistrarGasto


class SpendingListView(ListView):
    queryset = Gasto.objects.all().order_by('fecha_gasto')
    template_name = "gastos.html"

    def get(self, request, *args, **kwargs):
        gastos = Gasto.objects.all()
        total_gastos = Gasto.objects.all().count
        total_value = Gasto.objects.filter(precio__isnull=False).aggregate(Sum('precio'))

        context = {'total':gastos,
                    'total_gastos':total_gastos,
                    'total_value':total_value,
                    }
        return render(request,self.template_name, context)

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