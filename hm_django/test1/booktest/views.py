from django.shortcuts import render
# from  django.http import  request,response
from  django.http import *

def index(request):
    return HttpResponse('hello world')

# Create your views here.
