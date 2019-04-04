import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.validators import UniqueValidator

from users.models import Department, Employee



class EmployeeSerializer(serializers.Serializer):

    choices_gender = (
        (0, '男'),
        (1, '女'),
    )

    name = serializers.CharField(label='姓名', max_length=20)
    age = serializers.IntegerField(label='年龄')
    gender = serializers.ChoiceField(label='性别', default=0, choices=choices_gender)
    salary = serializers.DecimalField(label='工资', max_digits=8, decimal_places=2)
    comment = serializers.CharField(label='备注', max_length=300, allow_null=True, allow_blank=True)
    hire_date = serializers.DateField(label='入职时间')


    # 关联属性
    # 方式一：　序列化为主键ｉｄ返回回去
    department = serializers.PrimaryKeyRelatedField(label='所属部门', read_only=True)
    # 方式二：　序列化部门对象所有字段
    # department = DepartmentSerializer()




class DepartmentSerializer(serializers.Serializer):
    """
    序列化器:
    1. 转成字典的属性
    2. 校验的参数
    """
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20, label='部门名称')
    create_date = serializers.DateField(label='成立时间')
    is_delete = serializers.BooleanField(default=False, label='是否删除')


    # 关联属性序列化：
    # 方式一：　序列化主键 by evan
    # employee_set = serializers.PrimaryKeyRelatedField(label='部门员工', read_only=True, many=True)
    # 方式一:
    employee_set = EmployeeSerializer(many=True, read_only=True)




"""
# 序列化: 对象
from users.models import *
from users.serializers import *
dep = Department.objects.get(id=1)
serializer = DepartmentSerializer(dep)
print(serializer.data)
"""

"""
{
  "id": 1,
  "name": "赵小一",
  "age": 28,
  "gender": 0,
  "salary": "12000.00",
  "comment": null,
  "hire_date": "2011-01-01",
  "department": {
      "name": "xx",
      "create_date": "2018-1-1"
  },
}

"""