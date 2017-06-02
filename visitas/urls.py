from django.conf.urls import url
from visitas.views import VisitListView, CreateVisitView

urlpatterns = [
    url(r'^lista.visitas/$', VisitListView.as_view(), name='list_visitas'),
    url(r'^registro.visita/$', CreateVisitView.as_view(), name='registervisit.url'),
]