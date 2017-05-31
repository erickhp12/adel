from django.shortcuts import render
from django.views.generic import View, FormView
from .models import Paciente
from .forms import RegistrarPaciente


class PacienteListView(View):
    template_name = "pacientes.html"

    def get(self, request, *args, **kwargs):
        pacientes_registrados = Paciente.objects.all()
        return render(request, self.template_name, {
            'pacientes': pacientes_registrados,
            'message': 'Aqui andamos'
        })

class PatientDetailView(View):
    template_name = "paciente_detalle.html"

    def get(self, request, *args, **kwargs):
        id_paciente = self.kwargs['pk']
        print "ARGS " + str(id_paciente)
        pacientes_registrados = Paciente.objects.get(pk=id_paciente)
        return render(request, self.template_name, {
            'paciente': pacientes_registrados,
            'message': 'Aqui andamos'
        })

class CreatePatientView(FormView):
    template_name = "creacion_pacientes.html"
    message = "Aqui andamos al cien"

    def get(self, request, *args, **kwargs):
        form = RegistrarPaciente()
        data = {
            'form': form
        }
        return render(request,  self.template_name,  data)

    def post(self, request, *args, **kwargs):
        form = RegistrarPaciente(request.POST)
        data = {
            'form': form,
        }
        if form.is_valid():
            form.save(commit=True)
            message = "Agregado correctamente"
            data = {
                'form': form,
                'message': message
            }
            return render(request, self.template_name, data)
        else:
            message = "Faltan campos por llenar"
            data = {
                'form': form,
                'message': message,
            }
            return render(request, self.template_name, data)
