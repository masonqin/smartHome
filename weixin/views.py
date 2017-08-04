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
import ServerHelper

    
def WeChat(request):
  if request.method == 'GET':
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')

    if not wechat_instance.check_signature(
      signature=signature, timestamp=timestamp, nonce=nonce):
      return HttpResponseBadRequest('Verify Failed')

    return HttpResponse(
      request.GET.get('echostr', ''), content_type="text/plain")

def Emma(request):
  html = "<html><body><h1>Hello Emma</h1><h2>I love you!</h2></body></html>"
  return HttpResponse(html)

def Server(request):

  command = request.GET.get('cmd')
  ret = "command error"
  if command == "serveron":
    ServerHelper.WOL('D050995C9BC8')
    ret = "server is on"

  if command == "serveroff":
    ServerHelper.ShutDown()
    ret = "server is off"

  return HttpResponse(ret)