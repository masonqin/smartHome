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

    
def WeChat(request):
  if request.method == 'GET':
    # 检验合法性
    # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')

    if not wechat_instance.check_signature(
      signature=signature, timestamp=timestamp, nonce=nonce):
      return HttpResponseBadRequest('Verify Failed')

    return HttpResponse(
      request.GET.get('echostr', ''), content_type="text/plain")


