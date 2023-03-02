from django.http import JsonResponse


def django_jsonResponse_error(param):
    response = {'resultCode': "99999", 'resultMessage': param, 'resultData': {}}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


def django_jsonResponse_success(param, result_message):
    response = {'resultCode': '0', 'resultMessage': result_message, "resultData": param}
    return JsonResponse(response)
