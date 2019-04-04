from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from users.models import Department, Employee
from users.serializers import DepartmentSerializer, EmployeeSerializer#, DepartmentSerializer2, EmployeeSerializer2


def index(request):
    return HttpResponse('首页')


def department(request):
    # # 序列化:　对象
    # dep = Department.objects.get(id=1)
    # serializer = DepartmentSerializer(dep)
    # return JsonResponse(serializer.data)   # 传入字典数据

    # # 序列化:　查询集
    query_set = Department.objects.all()
    # 传递非对象数据时，需要指定many=True
    serializer = DepartmentSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)   # 传入字典数据


def employee(request):
    dep = Employee.objects.get(id=1)
    serializer = EmployeeSerializer(dep)
    return JsonResponse(serializer.data)   # 传入字典数据

