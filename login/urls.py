from django.conf.urls import url

from login.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index.view.url'),
]
