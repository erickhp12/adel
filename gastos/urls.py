from django.conf.urls import url
from gastos.views import SpendingListView, CreateSpendingView, DetailSpendingView, UpdateSpendingView

urlpatterns = [
    url(r'^lista.gastos/$', SpendingListView.as_view(), name='list_gastos'),
    url(r'^registro.gastos/$', CreateSpendingView.as_view(), name='registerSpending.url'),
    url(r'^gastos/ver/(?P<pk>\d+)/$',DetailSpendingView.as_view(),name='ver_gasto'),
	url(r'^gastos/editar/(?P<pk>\d+)/$', UpdateSpendingView.as_view(),name='editar_gasto'),
]