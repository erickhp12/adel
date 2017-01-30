from django.conf.urls import url
#from . import views
from empleados.views import *

app_name = 'empleados'

urlpatterns = [
    url(r'^$', EmployeeListView.as_view(), name='list'),
    url(r'^registro/$', CreateEmployeeView.as_view(), name='create.employee.url'),
]
