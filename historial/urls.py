from django.conf.urls import url

from historial.views import Requests

urlpatterns = [
    url(r'^request/$', Requests.as_view()),
]
