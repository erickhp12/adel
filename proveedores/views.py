from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Proveedor
from .forms import RegistrarProveedor
from django.http import HttpResponse


class ProviderListView(ListView):
    queryset = Proveedor.objects.all()
    template_name = "proveedores.html"

    def get_context_data(self, **kwargs):
        context = super(ProviderListView, self).get_context_data(**kwargs)
        context['total'] = Proveedor.objects.all().count()
        return context

class CreateProviderView(CreateView):
    form_class = RegistrarProveedor
    template_name = "creacion_proveedores.html"
    success_url = reverse_lazy('list_proveedores')

class UpdateProviderView(UpdateView):
    model = Proveedor
    form_class = RegistrarProveedor
    template_name = "creacion_proveedores.html"
    success_url = reverse_lazy('list_proveedores')    


class DetailProviderView(DetailView):
    model = Proveedor
    template_name = "proveedor_detalle.html"


 

