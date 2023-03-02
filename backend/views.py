import json
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import backend.models
from backend.models import Link
from backend.utils.request_verify import request_verify
from backend.utils.result_utils import django_jsonResponse_success, django_jsonResponse_error


@csrf_exempt
def query_all_link(request):
    result_list = []
    total = 0
    error_message = ""
    try:
        if request.method == "GET":
            env = request.GET.get('env')
            page = request.GET.get('page')
            page_size = request.GET.get('pageSize')
            if page is None:
                page = 1
            if page_size is None:
                page_size = 10
            links = Link.objects.filter(env=env).order_by('-id')
            paginator = Paginator(links, page_size)
            format_list = json.loads(serializers.serialize('json', paginator.page(page)))
            total = paginator.count
            for item in format_list:
                model = item["fields"]
                model["linkId"] = item['pk']
                result_list.append(model)
        else:
            error_message = "请求方式错误"
    except Exception as e:
        error_message = str(e)
    if len(error_message) > 0:
        return django_jsonResponse_error(error_message)
    else:
        return django_jsonResponse_success({
            "list": result_list,
            "total": total
        }, "请求成功")


#
@csrf_exempt
@request_verify('post', ['linkUrl', 'linkDescription'])
def add_link(request):
    body = json.loads(request.body)
    link_url = body.get('linkUrl')
    link_description = body.get('linkDescription')
    user_name = body.get('userName')
    pass_word = body.get('passWord')
    env = body.get('env')
    backend.models.Link(
        linkDescription=link_description,
        linkUrl=link_url,
        userName=user_name,
        passWord=pass_word,
        env=env
    ).save()
    return django_jsonResponse_success({}, "addLinkSuccess")


@csrf_exempt
@request_verify('post', ['linkId'])
def delete_link(request):
    err_message = ""
    body = json.loads(request.body)
    link_id = body.get("linkId")
    env = body.get("env")
    try:
        exists = backend.models.Link.objects.filter(id=link_id, env=env).exists()
        if not exists:
            err_message = "该链接不存在"
        else:
            backend.models.Link.objects.filter(id=link_id).delete()
    except Exception as e:
        err_message = format(str(e))
    if len(err_message) > 0:
        return django_jsonResponse_error(err_message)
    else:
        return django_jsonResponse_success({}, result_message="deleteLinkSuccess")


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
