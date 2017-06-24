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

    def get(self, request, *args, **kwargs):
        proveedores = Proveedor.objects.all()
        total_proveedores = Proveedor.objects.all().count
        
        context = {'proveedores':proveedores,
                    'total_proveedores':total_proveedores,        
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        proveedor_input = request.POST.get('proveedor')

        proveedores = Proveedor.objects.all().filter(nombre__contains=proveedor_input
            ) | Proveedor.objects.all().filter(contacto__contains=proveedor_input)
        total_proveedores = proveedores.count()

        context = {'proveedores':proveedores,
                    'total_proveedores':total_proveedores
                    }
        
        return render(self.request, self.template_name, context)

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


 

