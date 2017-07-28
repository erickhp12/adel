from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Paciente
from visitas.models import Visitas
from historial.models import Historial
from .forms import RegistrarPaciente
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PatientListView(ListView):
    queryset = Paciente.objects.all()
    template_name = "pacientes.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        total = Paciente.objects.all()
        total_pacientes = Paciente.objects.all().count
        
        context = {'Paciente':total,
                    'total':total_pacientes,        
                    }

        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        paciente_input = request.POST.get('paciente')

        paciente = Paciente.objects.all().filter(nombres__icontains=paciente_input
            ) | Paciente.objects.all().filter(apellidos__icontains=paciente_input)
        total_paciente = paciente.count()

        context = {'Paciente':paciente,
                    'total':total_paciente
                    }
        
        return render(self.request, self.template_name, context)

class CreatePatientView(CreateView):
    form_class = RegistrarPaciente
    template_name = "creacion_pacientes.html"
    success_url = reverse_lazy('list_pacientes')

class UpdatePatientView(UpdateView):
    model = Paciente
    form_class = RegistrarPaciente
    template_name = "creacion_pacientes.html"
    success_url = reverse_lazy('list_pacientes')    


class DetailPatientView(DetailView):
    model = Paciente
    template_name = "paciente_detalle.html"

    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.all().filter(id=pk)
        historial = Historial.objects.get(paciente=pk)
        visitas = Visitas.objects.all().filter(paciente_id=pk)
        precio_pesos = 0
        precio_dolares = 0
        precio_total = 0
        
        # validaciones para check
        alergias_value = "unchecked"
        corazon_value = "unchecked"
        presion_arterial_value = "unchecked"
        diabetes_value = "unchecked"
        hepatitis_value = "unchecked"
        vih_value = "unchecked"
        embarazada_value = "unchecked"
        medicamentos_value = "unchecked"

        if historial.alergias == True:
            alergias_value = "checked"
        if historial.corazon == True:
            corazon_value = "checked"
        if historial.presion_arterial == True:
            presion_arterial_value = "checked"
        if historial.diabetes == True:
            diabetes_value = "checked"
        if historial.hepatitis == True:
            hepatitis_value = "checked"
        if historial.vih == True:
            vih_value = "checked"
        if historial.embarazada == True:
            embarazada_value = "checked"
        if historial.medicamentos == True:
            medicamentos_value = "checked"

        for visita in visitas:
            if visita.dolares == "Dolares":
                precio_dolares += visita.precio * settings.DIVISA
                print precio_dolares
            else:
                precio_pesos += visita.precio

        precio_total = precio_pesos + precio_dolares


        context = {'visitas':visitas,
                    'paciente':paciente,
                    'historial':historial,
                    'alergias_value':alergias_value,
                    'corazon_value':corazon_value,
                    'presion_arterial_value':presion_arterial_value,
                    'diabetes_value':diabetes_value,
                    'hepatitis_value':hepatitis_value,
                    'vih_value':vih_value,
                    'embarazada_value':embarazada_value,
                    'medicamentos_value':medicamentos_value,
                    'precio_total':precio_total,
                    }
        return render(request,self.template_name, context)


class DeletePatientView(ListView):
    template_name = "eliminar_paciente.html"

    def get(self, request, pk, **kwargs):
        paciente = Paciente.objects.all().filter(id=pk)

        context = {'paciente':paciente}

        return render(request,self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        Paciente.objects.all().filter(id=pk).delete()

        return render(self.request,'pacientes.html')

 

