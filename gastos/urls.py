from django.conf.urls import url
from gastos.views import *

urlpatterns = [
    url(r'^lista.gastos/$', SpendingListView.as_view(), name='list_gastos'),
    url(r'^registro.gastos/$', CreateSpendingView.as_view(), name='registerSpending.url'),
    url(r'^gastos/ver/(?P<pk>\d+)/$',DetailSpendingView.as_view(),name='ver_gasto'),
	url(r'^gastos/editar/(?P<pk>\d+)/$', UpdateSpendingView.as_view(),name='editar_gasto'),
	url(r'^gastos/borrar/(?P<pk>\d+)/$', DeleteSpendingView.as_view(),name='borrar_gasto'),
	url(r'^movimientos/$', MovementsView.as_view(),name='movimientos'),
]