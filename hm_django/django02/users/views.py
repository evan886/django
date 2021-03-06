from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from decorators import check_ip



def index(request):

    return HttpResponse('首页')
# Create your views here.

# def resp(request):
#     """演示响应对象的使用"""
#     response = HttpResponse(content='<h3>首页</h3>',content_type='text/html', status=200)
#     response['category'] = 2
#     response['name'] = 'django'
#
#     return response


def resp(request):
    """演示响应对象的使用"""
    print('======resp======')
    #JsonResponse
    #context = [{'name':'django', 'age':20},{'name':'django2', 'age':20}]
    #return JsonResponse(context, safe=False)

    #重定向
    #return redirect('/index')
    #return HttpResponseRedirect('/index')
    #/users/index
    url = reverse('users:index')
    print(url)
    return redirect(url)


def get_cookie(request):
    """获取cookie键值对数据 请求对象读取"""

    user_id = request.COOKIES.get('user_id')
    user_name = request.COOKIES.get('user_name')
    text = 'user_id=%s, user_name=%s' % (user_id, user_name)
    return HttpResponse(text)


def set_cookie(request):
    """保存cookie键值对数据  响应对象保存"""
    # user_id=10
    # user_name=python
    response = HttpResponse('保存cookie成功')
    response.set_cookie('user_id', 10, 60*5)  # 参数3:有效期
    response.set_cookie('user_name', 'python')
    return response

def set_session(request):
    """保存session键值对数据"""

    request.session['user_id'] = 10
    request.session['user_name'] = 'Django'
    return HttpResponse('保存session键值对数据成功')


def get_session(request):
    """读取session键值对数据"""

    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')

    text = 'session数据: user_id=%s, user_name=%s' % (user_id, user_name)
    return HttpResponse(text)

# def post(request):
#     """显示发帖界面"""
#     return render(request, 'post.html')
# def do_post(request):
#     """执行发帖操作"""
#
#     # 获取帖子标题和内容
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#
#     return HttpResponse('发帖成功: %s %s' % (title, content))


@check_ip #== check_ip(post)
def post(request):
    """显示发帖界面"""
    if request.method == 'GET':
        return render(request, 'post.html')
    else:  # POST
        # 获取帖子标题和内容
        title = request.POST.get('title')
        content = request.POST.get('content')
        return HttpResponse('发帖成功: %s %s' % (title, content))

# /post2
class PostView(View):

    def get(self, request):
        return render(request, 'post2.html')

    # @method_decorator(check_ip)
    def post(self, request):
        # 获取帖子标题和内容
        title = request.POST.get('title')
        content = request.POST.get('content')
        return HttpResponse('发帖成功: %s %s' % (title, content))

class CheckIpMixin(object):

    """扩展类:扩展了一个检测ip是否为黑名单的功能"""
    @method_decorator(check_ip)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
