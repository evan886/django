from rest_framework import serializers


class DepartmentSerializer(serializers.Serializer):
    """
    序列化器:
    1. 转成字典的属性
    2. 校验的参数
    """
    id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=10, label='部门名称')
    # 参数校验方式1: 通过字段和选项来校验
    name = serializers.CharField(max_length=10, label='部门名称')
    # \u4e00-\u9fa5:中文
    # name = serializers.RegexField('^[a-zA-Z0-9\u4e00-\u9fa5]$',
    #                               max_length=10, label='部门名称',
    #                               validators=[UniqueValidator(queryset=Department.objects.all())])
    create_date = serializers.DateField(label='成立时间')
    is_delete = serializers.BooleanField(default=False, label='是否删除', required=False)


class EmployeeSerializer(serializers.Serializer):


    choices_gender = (
        (0, '男'),
        (1, '女'),
    )

    id = serializers.IntegerField(read_only=True)
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
