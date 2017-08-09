from django.conf.urls import url
from empleados.views import *

urlpatterns = [
    url(r'^lista.empleados/$', EmployeeListView.as_view(), name='list_empleados'),
    url(r'^registro.empleado/$', CreateEmployeeView.as_view(), name='registeremployee.url'),
	url(r'^empleados/editar/(?P<pk>\d+)/$',UpdateEmployeeView.as_view(),name='editar_empleado'),
	url(r'^empleados/borrar/(?P<pk>\d+)/$',DeleteEmployeeView.as_view(),name='borrar_empleado'),
]
