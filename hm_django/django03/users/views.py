from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.base import Template
from django.utils.timezone import now

from users.models import Department


class Student(object):

    #name='aaa'

    def name(self):
        return  'aaa2'


def index(request):

    # 使用模板
    # 模板使用的字典数据
    context = {
        'name': 'django',
        'my_obj': Student(),
        'my_list': [1, 2, 3, 4],
        'my_date': now(),
        'my_dict': {
            'name': 'python',
            'age': 20,
            'gender': '男',
        }
    }
    ## 方式一
    #return  render(request,'index.html',context)



    # 方式二：
    # 获取Template对象
    template = loader.get_template('index.html')  # type: Template
    # 渲染模板,生成html字符串
    html_str = template.render(context)
    return HttpResponse(html_str)
