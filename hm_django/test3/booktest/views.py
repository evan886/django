#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return HttpResponse('hello world')
'''
#其实就是 关键参数 
urls.py 如下 
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$',views.detail,name='detail'),
'''



def detail(request,p1):
    return HttpResponse(p1)
