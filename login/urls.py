from django.conf.urls import url

from login.views import IndexView, LoginView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index.view.url'),
    url(r'^login/$', LoginView.as_view(), name='login.view.url'),
]
