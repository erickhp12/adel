from django.conf.urls import url
from gastos.views import *

urlpatterns = [
    url(r'^lista.gastos/$', SpendingListView.as_view(), name='list_gastos'),
    url(r'^registro.gasto/$', CreateSpendingView.as_view(), name='registerSpending.url'),
	url(r'^gastos/editar/(?P<pk>\d+)/$', UpdateSpendingView.as_view(),name='editar_gasto'),
	url(r'^movimientos/$', MovementsView.as_view(),name='movimientos'),
]