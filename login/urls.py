from django.conf.urls import url

from login.views import IndexView, LoginView, LogoutView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index.view.url'),
    url(r'^login/$', LoginView.as_view(), name='login.view.url'),
    url(r'^logout/$', LogoutView.as_view(), name='logout.view.url'),
]
