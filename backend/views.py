import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from backend.models import Link


def query_all_link(request):
    response = {}
    try:
        links = Link.objects.filter()
        response['list'] = json.loads(serializers.serialize('json', links))
        response['resultCode'] = '200'
        response['resultMessage'] = 'success'

    except Exception as e:
        response['resultCode'] = '9999999'
        response['resultMessage'] = str(e)
    return JsonResponse(response)
