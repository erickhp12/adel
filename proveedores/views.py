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


class ProviderListView(ListView):
    template_name = "proveedores.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        proveedores = Proveedor.objects.filter(user=request.user)
        total_proveedores = proveedores.count
        mensaje = ""
        context = {'proveedores':proveedores,
                    'total_proveedores':total_proveedores,
                    'mensaje': mensaje        
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        proveedor_input = request.POST.get('proveedor')
        mensaje = ""
        proveedores = Proveedor.objects.all().filter(nombre__icontains=proveedor_input
            ) | Proveedor.objects.all().filter(contacto__icontains=proveedor_input)
        total_proveedores = proveedores.count()

        if total_proveedores == 0:
            mensaje = "La busqueda no mostro ningun resultado"

        context = {'proveedores':proveedores,
                    'total_proveedores':total_proveedores,
                    'mensaje': mensaje
                    }
        
        return render(self.request, self.template_name, context)


class CreateProviderView(CreateView):
    template_name = "creacion_proveedores.html"
    template_main = "proveedores.html"

    def get(self, request, *args, **kwargs):
        user_logged = request.user
        proveedores = Proveedor.objects.filter(user=request.user)
        total_proveedores = proveedores.count
        mensaje = ""
        context = {'proveedores': proveedores,
                   'total_proveedores': total_proveedores,
                   'mensaje': mensaje
                   }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        proveedores = Proveedor.objects.filter(user=request.user)
        total_proveedores = proveedores.count
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
                   'total_proveedores': total_proveedores,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.proveedores')


class UpdateProviderView(View):
    template_name = "edicion_proveedores.html"
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
        total_proveedores = proveedores.count
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
            mensaje = "Error al editar empleado " + str(e)

        context = {'proveedores': proveedores,
                   'total_proveedores': total_proveedores,
                   'mensaje': mensaje
                   }

        return HttpResponseRedirect('/lista.proveedores')


class DeleteProviderView(ListView):
    template_name = "eliminar_proveedor.html"

    def get(self, request, pk, **kwargs):
        proveedor = Proveedor.objects.all().filter(id=pk)

        context = {'proveedor':proveedor}

        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        mensaje = ""
        proveedores = Proveedor.objects.filter(user=request.user)
        total_proveedores = proveedores.count
        Proveedor.objects.all().filter(id=pk).delete()

        context = {'proveedores': proveedores,
                   'total_proveedores': total_proveedores,
                   'mensaje': mensaje
                   }

        return render(self.request,'proveedores.html', context)


 

