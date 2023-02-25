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
    link_url = request.POST.get('linkUrl')
    link_description = request.POST.get('linkDescription')
    link_remark = request.POST.get('linkRemark')
    user_name = request.POST.get('userName')
    pass_word = request.POST.get('passWord')
    err_message = ""

    if link_url == "":
        err_message = "请输入链接"
    if link_description == "":
        err_message = "请输入链接描述"
    if link_remark == "":
        err_message = "请输入链接备注"

    if err_message != "":
        response['resultCode'] = '9999999'
        response['resultMessage'] = err_message
    if err_message == "":
        backend.models.Link(
            linkDescription=link_description,
            linkRemark=link_remark,
            linkUrl=link_url,
            userName=user_name,
            passWord=pass_word
        ).save()
        response['resultCode'] = '0'
        response['resultMessage'] = "addLink Success"
    return JsonResponse(response)


@csrf_exempt
def delete_link(request):
    response = {}
    err_message = ""
    link_id = request.POST.get("linkId")
    if link_id == "":
        err_message = "请输入对应的id"
    try:
        target_one = Link.objects.get(id=link_id)
        if target_one.linkUrl == "":
            err_message = '查找不到对应的数据'
    except Exception as e:
        err_message = format(str(e))
    if err_message != "":
        response['resultCode'] = '9999999'
        response['resultMessage'] = err_message
    else:
        backend.models.Link.objects.filter(id=link_id).delete()
        response['resultCode'] = '0'
        response['resultMessage'] = 'delete success'
    return JsonResponse(response)
