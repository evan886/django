import json

from django.http.response import HttpResponse
from django.shortcuts import render


# # /users/index
# def index(request):
#     """视图:显示首页"""
#     # request: HttpRequest类型
#     # ctrl + alt/win + 空格
#     return HttpResponse('<h3>首页<h3/>')


def index(request):
    """视图:显示首页"""
    # render: 返回HttpResponse对象

    # aa = None
    # print('aa=' + aa)

    # 获取request中的属性
    path = request.path
    method = request.method
    print(path, method)
    # users = request.users
    # authenticated: 认证,登录
    # 已登录：AbstractUser对象；
    # 未登录：AnonymousUser对象
    if request.user.is_authenticated(): #
        print('已登录: %s' % request.user.username)
    else:
        print('未登录: %s' % request.user)


    return render(request, 'index.html')
    # return render(request, 'users/index2.html')


# news/1/2
def news(request, page, category):
    """
    显示新闻
    :param category: 类别id
    :param page: 第几页数据
    """
    text = 'category=%s, page=%s'\
           % (category, page)
    return HttpResponse(text)


# /news2?category=1&page=2
def news2(request):
    """显示新闻: 获取查询字符串中的值"""

    category = request.GET.get('category')
    page = request.GET.get('page')
    a = request.GET.getlist('a')
    print(a)

    text = 'news2: category=%s, page=%s' \
           % (category, page)
    return HttpResponse(text)


def news3(request):
    """显示新闻: 获取body中的键值对数据(提交表单)"""
    category = request.POST.get('category')
    page = request.POST.get('page')
    a = request.POST.getlist('a')
    print(a)

    text = 'news3: category=%s, page=%s' \
           % (category, page)
    return HttpResponse(text)


def news4(request):
    """显示新闻:
    1. 获取并解析json字符串
    2. 获取请求头中的数据
    """
    ip = request.META.get('REMOTE_ADDR')
    length = request.META.get('CONTENT_LENGTH')
    # 获取请求头属性值时，需要添加前缀 HTTP_ 并转成大写，作为键来获取值
    category = request.META.get('HTTP_CATEGORY')
    page = request.META.get('HTTP_PAGE')

    text = 'ip=%s, length=%s, category=%s, page=%s'\
           %(ip,  length, category, page)
    print(text)


    # 获取body中的json字符串: {"category":1, "page":2}
    json_str = request.body.decode()
    # jsons -> 字典
    dict_data = json.loads(json_str)
    category = dict_data.get('category')
    page = dict_data.get('page')

    # 返回响应对象
    text = 'news4: category=%s, page=%s' \
           % (category, page)
    return HttpResponse(text)








#floating 就是浮起了 哈哈哈 不错




