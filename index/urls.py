from django.conf.urls import url
from index.views import IndexView

urlpatterns = [
    url(r'^inicio/$', IndexView.as_view(), name='index.url')
]