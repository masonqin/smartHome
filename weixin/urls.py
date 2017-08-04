from django.conf.urls import include, url
from .views import WeChat,emma,server

urlpatterns = [
    url(r'^weixin/', WeChat),
    url(r'^emma/', emma),
    url(r'^server/', server),
]