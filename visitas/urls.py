from django.conf.urls import url
from visitas.views import *

urlpatterns = [
    url(r'^lista.visitas/$', VisitListView.as_view(), name='list_visitas'),
    url(r'^registro.visita/$', CreateVisitView.as_view(), name='registerVisit.url'),
    url(r'^visitas/ver/(?P<pk>\d+)/$',DetailVisitView.as_view(),name='ver_visita'),
	url(r'^visitas/editar/(?P<pk>\d+)/$', UpdateVisitView.as_view(),name='editar_visita'),
	url(r'^visitas/borrar/(?P<pk>\d+)/$', DeleteVisitView.as_view(),name='borrar_visita'),
]