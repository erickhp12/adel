from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, View
from django.core.urlresolvers import reverse_lazy
from .models import Proveedor
from .forms import RegistrarProveedor
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ProviderListView(ListView):
    template_name = "proveedores.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        QueryProveedores = Proveedor.objects.filter(user=request.user)
        total = QueryProveedores.count()
        mensaje = ""
        paginator = Paginator(QueryProveedores, 50)
        page = request.GET.get('page')
        
        try:
            proveedores = paginator.page(page)
        except PageNotAnInteger:
            proveedores = paginator.page(1)
        except EmptyPage:
            proveedores = paginator.page(paginator.num_pages)

        
        if total == 0:
            mensaje = "No tienes proveedores registrados"

        context = {
                    'proveedores':proveedores,
                    'total':total,
                    'mensaje': mensaje        
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        proveedor_input = request.POST.get('proveedor')
        mensaje = ""
        proveedores = Proveedor.objects.all().filter(nombre__icontains=proveedor_input,user=request.user
            ) | Proveedor.objects.all().filter(contacto__icontains=proveedor_input,user=request.user)
        total = proveedores.count()

        if total == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = {'proveedores':proveedores,
                    'total':total,
                    'mensaje': mensaje
                    }
        
        return render(self.request, self.template_name, context)


class CreateProviderView(CreateView):
    template_name = "proveedores-formulario.html"
    template_main = "proveedores.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        proveedores = Proveedor.objects.filter(user=request.user).order_by('-fecha_inicio')
        total = proveedores.count
        mensaje = ""
        
        context = {'proveedores': proveedores,
                   'total': total,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        proveedores = Proveedor.objects.filter(user=request.user)
        total = proveedores.count
        user = request.user
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        producto = request.POST.get('producto')

        
        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                Proveedor.objects.create(
                    user=user,
                    nombre=nombre,
                    contacto=contacto,
                    producto=producto,
                    telefono=telefono,
                    correo=correo,
                    direccion=direccion
                )
        except Exception as e:
            mensaje = "Error al crear proveedor " + str(e)

        context = {'proveedores': proveedores,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.proveedores')


class UpdateProviderView(View):
    template_name = "proveedores-formulario.html"
    template_main = "proveedores.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        proveedor = Proveedor.objects.get(user=request.user,id=pk)
        mensaje = ""
        context = {'proveedor': proveedor,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request,pk, *args, **kwargs):
        mensaje = ""
        proveedores = Proveedor.objects.filter(user=request.user)
        total = proveedores.count
        user = request.user
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        producto = request.POST.get('producto')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')

        try:
            if nombre == "":
                return render(self.request, self.template_name)
            else:
                proveedor = Proveedor.objects.get(user=request.user,id=pk)
                proveedor.nombre = nombre
                proveedor.contacto = contacto
                proveedor.producto = producto
                proveedor.telefono = telefono
                proveedor.correo = correo
                proveedor.direccion = direccion
                proveedor.save()
        except Exception as e:
            mensaje = "Error al editar proveedor " + str(e)

        context = {'proveedores': proveedores,
                   'total': total,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.proveedores')

class DeleteProviderView(ListView):
    
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, pk, **kwargs):
        Proveedor.objects.filter(id=pk,user=request.user).delete()

        return render(request,'proveedores.html')
