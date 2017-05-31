from django.conf.urls import url
from pacientes.views import PacienteListView, PatientDetailView,CreatePatientView

urlpatterns = [
    url(r'^lista.pacientes/$', PacienteListView.as_view(), name='list'),
    url(r'^paciente.detalle/(?P<pk>[0-9]+)/$', PatientDetailView.as_view(), name='list'),
    url(r'^registro.paciente/$', CreatePatientView.as_view(), name='registerpatient.url')
]
