from django.conf.urls import url
from agenda.views import AgendaListView, CreateAgendaView

urlpatterns = [
    url(r'^lista.agenda/$', AgendaListView.as_view(), name='list_agenda'),
	url(r'^registro.agenda/$', CreateAgendaView.as_view(), name='registerAgenda.url'),
	# url(r'^proveedores/ver/(?P<pk>\d+)/$',DetailProviderView.as_view(),name='ver_proveedor'),
	# url(r'^proveedores/editar/(?P<pk>\d+)/$',UpdateProviderView.as_view(),name='editar_proveedor'),
]