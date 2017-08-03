from django.conf.urls import url
from historial.views import *

urlpatterns = [
    url(r'^request-historial/$', RequestHistorial.as_view()),
    url(r'^historial/editar/(?P<pk>\d+)/$', CreateHistoryView.as_view(), name='registerhistory.url'),
]
