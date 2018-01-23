from django.conf.urls import url
from recetas.views import *

urlpatterns = [
    url(r'^lista.recetas/$', ReceiptListView.as_view(), name='list_recetas'),
    url(r'^registro.recetas/$', CreateReceiptView.as_view(), name='registerVisit.url')
]