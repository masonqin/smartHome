from django.conf.urls import include, url
from .views import WeChat
from .views import Emma

urlpatterns = [
    url(r'^$', WeChat),
    url(r'^emma/', Emma),
]