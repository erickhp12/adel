from django.conf.urls import url
from visitas.views import *

urlpatterns = [
    url(r'^lista.visitas/$', VisitListView.as_view(), name='list_visitas'),
    url(r'^registro.visita/$', CreateVisitView.as_view(), name='registerVisit.url'),
	url(r'^visitas/editar/(?P<pk>\d+)/$', UpdateVisitView.as_view(),name='editar_visita'),
]