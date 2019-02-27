from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from .models import Netstatus
import datetime
import json
from django.core import serializers
import requests
# Create your views here.

def get_geo_address(ip_address):
    api_address = 'http://freeapi.ipip.net/'
    request_url = api_address+ip_address
    try:
        res = requests.get(request_url)
        res.raise_for_status()
        return res.text
    except :
        return 'Unknown'

def index(request):
    latest_update_queryset = Netstatus.objects.all().order_by('-pk')
    data = serializers.serialize("json", latest_update_queryset)
    return HttpResponse(data)

def update(request,device='Unknown'):
    nets = Netstatus()
    nets.device = device
    # nets.updatetime = datetime.datetime.strdatetime('%c',datetime.datetime.now())
    nets.updatetime = str(datetime.datetime.now())
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ipaddress =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ipaddress = request.META['REMOTE_ADDR']

    nets.ipadress = ipaddress
    nets.geoadress = get_geo_address(ipaddress)

    nets.save()
    return HttpResponse(nets)

