from django.conf.urls import url
from proveedores.views import CreateProviderView, ProviderListView, DetailProviderView, UpdateProviderView

urlpatterns = [
    url(r'^lista.proveedores/$', ProviderListView.as_view(), name='list_proveedores'),
    url(r'^registro.proveedor/$', CreateProviderView.as_view(), name='registerProvider.url'),
	url(r'^proveedores/ver/(?P<pk>\d+)/$',DetailProviderView.as_view(),name='ver_proveedor'),
	url(r'^proveedores/editar/(?P<pk>\d+)/$',UpdateProviderView.as_view(),name='editar_proveedor'),
]