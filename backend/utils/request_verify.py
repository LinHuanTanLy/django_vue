# -*- coding: utf-8 -*-
# @Author   : 不言
# @Time     : 2020/8/28 2:40 下午
from functools import wraps

from backend.utils.result_utils import django_jsonResponse_error
import json


def request_verify(request_method: str, need_params=None):
    """
    在views方法上加装饰器 例如：@request_verify('get', ['id'])
    :param request_method:
    :param need_params:
    :return:
    """

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            method = str(request.method).lower()

            # 先判断类型，类型不符合，直接return
            if request_method and not method == request_method.lower():
                response = django_jsonResponse_error(" method %s not allowed for: %s" %
                                                     (request.method, request.path))
                return response

            request.params = {}

            # 暂时不用get请求传参，get的情况可以先忽略
            if method == 'get':
                if not request.GET:  # xxx.com或xxx.com/xx/?
                    if need_params:
                        response = django_jsonResponse_error("缺少参数！")
                        return response
                else:
                    params = {}
                    request_params = request.GET
                    for item in request_params:
                        params.update({item: request_params.get(item)})
                request.params = params

            else:  # method == post
                if not request.body or request.body == {}:  # 参数为空的情况下
                    if need_params:  # 验证必传
                        response = django_jsonResponse_error("缺少参数！")
                        return response
                else:
                    # 非空的时候，尝试去获取参数
                    try:
                        # 这边要try一下，如果前端传参不是json，json.loads会异常
                        real_request_params = json.loads(request.body)
                    except Exception as e:
                        response = django_jsonResponse_error("参数格式不合法！")
                        return response

                    # 取出来以后再去判断下必填项是否每一项都有值
                    if need_params:
                        for need_param_name in need_params:
                            if not real_request_params.get(need_param_name):
                                # 如果必传参数取出来是'' (PS: 没传和传了''通过get取出来都是'')，就抛出
                                response = django_jsonResponse_error(
                                    " 参数 %s 不能为空" % need_param_name)
                                return response

                    # 一直到这里都无异常那么就可以把参数塞进request对象了，避免view里还要再去json.loads
                    request.params = real_request_params

            return func(request, *args, **kwargs)

        return inner

    return decorator
