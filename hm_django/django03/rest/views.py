import json

from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet

#from rest.serializers import DepartmentSerialiser
from users.models import Department
'''
1. 查询所有部门  GET     /departments/
2. 新增一个部门  POST    /departments/

3. 查询一个部门  GET     /departments/<pk>/
4. 修改一个部门  PUT     /departments/<pk>/
5. 删除一个部门  DELETE  /departments/<pk>/
'''

# 列表视图
# 查询所有部门  GET     /departments/
# 新增一个部门  POST    /departments/
class DepartmentListView(View):

    def get(self, request):
        # 查询所有部门  GET     /departments/
        # 1. 查询所有的部门

        #在models中注释  manager = DepartmentManager()  AttributeError: type object 'Department' has no attribute 'objects'
        query_set = Department.objects.all()
        # 2. 查询集 -> 列表
        my_list = []
        for dep in query_set:
            dict_data = {
                'id': dep.id,
                'name': dep.name,
                'create_date': dep.create_date,
            }
            my_list.append(dict_data)
        # context = {
        #     'department': my_list
        #}
        #3. 返回响应对象(列表 -> json)
        return JsonResponse(my_list, safe=False)


    def post(self, request):
        # 新增一个部门  POST    /departments/
        # 1. 获取请求的参数(json):
        #    {'name':'研发部', 'create_date': '2018-1-1'}
        json_str = request.body.decode()
        # 2. json -> 字典
        dict_data = json.loads(json_str)
        # 3. 校验参数合法性(略)
        # 4. 业务操作(保存一个部门)
        dep = Department()
        dep.name = dict_data.get('name')
        dep.create_date = dict_data.get('create_date')
        dep.save()
        # 5. 部门对象 -> 字典
        dict_data = {
            'id': dep.id,
            'name': dep.name,
            'create_date': dep.create_date,
        }
        # 6. 返回响应对象, 增删成功返回201状态码
        return JsonResponse(dict_data, status=201)


# 详情视图
# 查询一个部门  GET     /departments/<pk>/
# 修改一个部门  PUT     /departments/<pk>/
# 删除一个部门  DELETE  /departments/<pk>/
class DepartmentDetailView(View):
    def get(self, request, id):
        # 查询一个部门  GET     /departments/<pk>/
        try:
            dep = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return HttpResponse(status=404)
        # 部门对象转字典
        dict_data = {
            'id': dep.id,
            'name': dep.name,
            'create_date': dep.create_date,
        }
        return JsonResponse(dict_data)

# on postman http://127.0.0.1:8000/departments/6/  put
    def put(self, request, id):
        # 修改一个部门  PUT     /departments/<pk>/
        # 1. 获取请求参数：json字符串
        json_str = request.body.decode()
        # 2. json -> 字典
        dict_data = json.loads(json_str)
        # 3. 校验参数合法性（略）
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return HttpResponse(status=404)  # 修改数据失败
        # 4. 操作数据库（修改数据）
        department.name = dict_data.get('name')
        department.create_date = dict_data.get('create_date')
        department.save()  # 修改操作
        # 5. 对象 -> 字典
        dict_data = {
            'id': department.id,
            'name': department.name,
            'create_date': department.create_date,
        }
        # 6. 返回响应对象: 字典 -> json
        return JsonResponse(dict_data)


    def delete(self, request, id):
        # 删除一个部门  DELETE  /departments/<pk>/
        try:
            dep = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return HttpResponse(status=404)
        # 删除一个部门
        dep.delete()
        # 删除成功返回204状态码
        return HttpResponse(status=204)