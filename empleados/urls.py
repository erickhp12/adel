from django.conf.urls import url
from empleados.views import CreateEmployeeView, EmployeeListView, DetailEmployeeView, UpdateEmployeeView

urlpatterns = [
    url(r'^lista.empleados/$', EmployeeListView.as_view(), name='list_empleados'),
    url(r'^registro.empleado/$', CreateEmployeeView.as_view(), name='registeremployee.url'),
	url(r'^empleados/ver/(?P<pk>\d+)/$',DetailEmployeeView.as_view(),name='ver_empleado'),
	url(r'^empleados/editar/(?P<pk>\d+)/$',UpdateEmployeeView.as_view(),name='editar_empleado'),
]
