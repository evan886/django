#-*- coding:utf-8 -*-

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return HttpResponse(request.path)


#
def getTest1(request):
    return render(request,'booktest/getTest1.html')

def getTest2(request):
    # print request.GET
    #根据键接收值
    a1=request.GET['a']
    b1=request.GET['b']
    c1=request.GET['c']
    #构造上下文
    context={'a':a1, 'b':b1, 'c':c1}
    return render(request,'booktest/getTest2.html',context)

def getTest3(request):
    #a1=request.GET['a'] #只得到最后的值
    a1 = request.GET.getlist('a')
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context) #居然写少context



def postTest1(request):
    return render(request,'booktest/postTest1.html')
def postTest1(request):
    return render(request,'booktest/postTest2.html')

'''
#其实就是 关键参数 
urls.py 如下 
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$',views.detail,name='detail'),
'''

def detail(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))


