from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Gasto
from .forms import RegistrarGasto


class SpendingListView(ListView):
    queryset = Gasto.objects.all().order_by('fecha_gasto')
    template_name = "gastos.html"

    def get_context_data(self, **kwargs):
        context = super(SpendingListView, self).get_context_data(**kwargs)
        context['total'] = Gasto.objects.all().count()
        return context

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