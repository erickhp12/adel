from django.conf.urls import url

from historial.views import RequestHistorial

urlpatterns = [
    url(r'^request-historial/$', RequestHistorial.as_view()),
]
