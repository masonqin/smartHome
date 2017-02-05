from django.conf.urls import include, url
from .views import WeChat

urlpatterns = [
    url(r'^weixin/', WeChat),
    url(r'^emma/', emma),
]