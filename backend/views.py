import json
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import backend.models
from backend.models import Link


@csrf_exempt
def query_all_link(request):
    response = {}
    try:
        if request.method == "GET":
            env = request.GET.get('env')
            page = request.GET.get('page')
            page_size = request.GET.get('pageSize')
            if page is None:
                page = 1
            if page_size is None:
                page_size = 10
            links = Link.objects.filter(env=env).order_by('id')
            paginator = Paginator(links, page_size)
            format_list = json.loads(serializers.serialize('json', paginator.page(page)))
            result_list = []
            for item in format_list:
                model = item["fields"]
                model["linkId"] = item['pk']
                result_list.append(model)
            response["resultData"] = {
                'list': result_list,
                "total": paginator.count
            }
            response['resultCode'] = '200'
            response['resultMessage'] = 'success'
        else:
            response['resultCode'] = '9999999'
            response['resultMessage'] = "请求方式错误"
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
        target_one = Link.objects.get(linkId=link_id)
        if target_one.linkUrl == "":
            err_message = '查找不到对应的数据'
    except Exception as e:
        err_message = format(str(e))
    if err_message != "":
        response['resultCode'] = '9999999'
        response['resultMessage'] = err_message
    else:
        backend.models.Link.objects.filter(linkId=link_id).delete()
        response['resultCode'] = '0'
        response['resultMessage'] = 'delete success'
    return JsonResponse(response)


@csrf_exempt
def update_link(request):
    response = {}
    link_url = request.POST.get('linkUrl')
    link_description = request.POST.get('linkDescription')
    link_remark = request.POST.get('linkRemark')
    user_name = request.POST.get('userName')
    pass_word = request.POST.get('passWord')
    link_id = request.POST.get('linkId')
    err_message = ""
    if link_id == "":
        err_message = "输入有误，请重新确认"
    try:
        target_one = Link.objects.get(linkId=link_id)
        if target_one.linkUrl == "":
            err_message = '找不到对应链接数据，请重新确认'
    except Exception as e:
        err_message = format(str(e))
    if err_message != "":
        response['resultCode'] = '9999999'
        response['resultMessage'] = err_message
    else:
        if link_url != "":
            target_one.linkUrl = link_url
        if link_remark != "":
            target_one.linkRemark = link_remark
        if link_description != "":
            target_one.linkDescription = link_description
        if user_name != "":
            target_one.userName = user_name
        if pass_word != "":
            target_one.passWord = pass_word
        target_one.save()
        response['resultCode'] = '0'
        response['resultMessage'] = "updateLink Success"
    return JsonResponse(response)
