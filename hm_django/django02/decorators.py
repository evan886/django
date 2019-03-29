from django.http.response import HttpResponse


def check_ip(fun_view):
    """装饰器: 禁止ip黑名单访问"""

    def wrapper(request, *args, **kwargs):
        # 获取访问用户的ip地址
        ip = request.META.get('REMOTE_ADDR')
        if ip in ['127.0.0.1']: # 如果在黑名单中
            return HttpResponse('ip禁止访问')

        return fun_view(request,*args, **kwargs)

    return wrapper# 最后显示这个 ip禁止访问