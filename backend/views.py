import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import backend.models
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


#
@csrf_exempt
def add_link(request):
    response = {}
    linkUrl = request.POST.get('linkUrl')
    linkDescription = request.POST.get('linkDescription')
    linkRemark = request.POST.get('linkRemark')
    userName = request.POST.get('userName')
    passWord = request.POST.get('passWord')
    errMessage = ""

    if linkUrl == "":
        errMessage = "请输入链接"
    if linkDescription == "":
        errMessage = "请输入链接描述"
    if linkRemark == "":
        errMessage = "请输入链接备注"

    if errMessage != "":
        response['resultCode'] = '9999999'
        response['resultMessage'] = errMessage
    if errMessage == "":
        backend.models.Link(
            linkDescription=linkDescription,
            linkRemark=linkRemark,
            linkUrl=linkUrl,
            userName=userName,
            passWord=passWord
        ).save()
        response['resultCode'] = '0'
        response['resultMessage'] = "addLink Success"
    return JsonResponse(response)
