from django.conf.urls import url
from pacientes.views import *

urlpatterns = [
    url(r'^lista.pacientes/$', PatientListView.as_view(), name='list_pacientes'),
    url(r'^registro.paciente/$', CreatePatientView.as_view(), name='registerPatient.url'),
	url(r'^pacientes/ver/(?P<pk>\d+)/$',DetailPatientView.as_view(),name='ver_paciente'),
	url(r'^pacientes/editar/(?P<pk>\d+)/$',UpdatePatientView.as_view(),name='editar_paciente'),
	url(r'^pacientes/borrar/(?P<pk>\d+)/$',DeletePatientView.as_view(),name='borrar_paciente'),
    url(r'^request-pacientes/$', RequestPaciente.as_view()),
]
