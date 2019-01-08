#-*- coding:utf-8 -*-
from django.shortcuts import render
from  django.http  import *
from .models import  *
# from  django.http import  request,response
#from django.template import RequestContext,loader

def index(request):
    #temp=loader.get_template('booktest/index.html')
    #return HttpResponse(temp.render())
    # 这样还要看一下 不全明白呢
    bookList=BookInfo.objects.all() #这行没效果 
    context ={'list':bookList} # 'bookList' 这样变成str了
    return render(request,'booktest/index.html',context )

def show(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    context={'list':herolist}
    return render(request,'booktest/show.html',context)


