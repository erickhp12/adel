from django.conf.urls import url
from recetas.views import *

urlpatterns = [
    url(r'^lista.recetas/$', ReceiptListView.as_view(), name='list_recetas'),
    url(r'^registro.receta/$', CreateReceiptView.as_view(), name='registerVisit.url'),
	url(r'^recetas/editar/(?P<pk>\d+)/$', UpdateReceiptView.as_view(),name='editar_receta')
]