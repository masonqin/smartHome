from django.shortcuts import render
# https://my.oschina.net/bxxfighting/blog/539968
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.template import loader, Context
from xml.etree import ElementTree as ET
import time
import hashlib


  # @csrf_exempt
  # def dispatch(self, *args, **kwargs):
  #   return super(WeChat, self).dispatch(*args, **kwargs)
    
def WeChat(request):
  
  # signature = request.GET.get('signature', None)
  # timestamp = request.GET.get('timestamp', None)
  # nonce = request.GET.get('nonce', None)
  # echostr = request.GET.get('echostr', None)

  # token = 'xiaochengqin'

  # hashlist = [token, timestamp, nonce]
  # hashlist.sort() 

  # hashstr = ''.join([s for s in hashlist])
  # hashstr = hashlib.sha1(hashstr).hexdigest()
  #tests
  # if hashstr == signature:
  html = "<html><body><h1>Hello Emma</h1><h2>I love you!</h2></body></html>"
  return HttpResponse(html)


