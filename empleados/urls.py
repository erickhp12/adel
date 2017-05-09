from django.conf.urls import url
from empleados.views import CreateEmployeeView, EmployeeListView

urlpatterns = [
    url(r'^lista.empleados/$', EmployeeListView.as_view(), name='list'),
    url(r'^registro/$', CreateEmployeeView.as_view(), name='registeremployee.url')
]
