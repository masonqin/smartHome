from django.conf.urls import include, url
from .views import WeChat,Emma,Server

urlpatterns = [
    url(r'^weixin/', WeChat),
    url(r'^emma/', Emma),
    url(r'^server/', Server),

]