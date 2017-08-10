from django.conf.urls import url
from agenda.views import *

urlpatterns = [
    url(r'^lista.agenda/$', AgendaListView.as_view(), name='list_agenda'),
	url(r'^registro.agenda/$', CreateAgendaView.as_view(), name='registerAgenda.url'),
	url(r'^agenda/editar/(?P<pk>\d+)/$',UpdateAgendaView.as_view(),name='editar_agenda'),
	url(r'^agenda/borrar/(?P<pk>\d+)/$',DeleteAgendaView.as_view(),name='borrar_agenda'),
]