from rest_framework import serializers
from users.models import  Department

class DepartmentSerialiser(serializers.ModelSerializer):
    """
    部门序列化器
    1. 对象与字典的转换
    2. 校验参数合法性
    3. 保存或修改数据
    """
    class Meta(object):
        model = Department
        # 针对模型所有的属性进行字典的转换
        fields = '__all__'