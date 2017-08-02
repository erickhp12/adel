from django.conf.urls import url
from proveedores.views import *

urlpatterns = [
    url(r'^lista.proveedores/$', ProviderListView.as_view(), name='list_proveedores'),
    url(r'^registro.proveedor/$', CreateProviderView.as_view(), name='registerProvider.url'),
	url(r'^proveedores/editar/(?P<pk>\d+)/$',UpdateProviderView.as_view(),name='editar_proveedor'),
	url(r'^proveedores/borrar/(?P<pk>\d+)/$',DeleteProviderView.as_view(),name='borrar_proveedor'),
]