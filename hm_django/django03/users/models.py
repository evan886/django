#--*--utf-8 --*--
from django.db import models
from django.db.models.manager import Manager


class DepartmentManager(Manager):
    """自定义模型管理器"""

    def all(self):
        """重写方法,改变返回的结果数据"""
        # 返回未删除的部门
        return super().all().filter(is_delete=False)

    def create_dep(self, name, create_date):
        """封装新增部门的方法，方便调用"""

        dep = Department()
        dep.name = name
        dep.create_date = create_date
        dep.save()
        return dep


class Department(models.Model):
    """部门模型类"""

    # 字符串类型,必须要指定max_length
    name = models.CharField(max_length=20)
    # 日期类型
    create_date = models.DateField(auto_now_add=True)
    # 逻辑删除标识
    is_delete = models.BooleanField(default=False)

    #location = models.CharField(max_length=20)


    # 自定义模型管理器, 自定义之后, Django默认的objects就不会自动创建了
    # manager = DepartmentManager()

    def __str__(self):
        return self.name

    class Meta:
        # 指定表名
        db_table = 'department'






class Employee(models.Model):
    """员工模型类"""

    choices_gender = (
        (0, '男'),
        (1, '女'),
    )
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # 性别 0表示男
    gender = models.IntegerField(default=0, choices=choices_gender)
    # 工资  999999.99
    # decimal_places 小数点位置
    # max_digits 总位置
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    # 备注: blank=True前端html界面，此字段可以不输入内容
    comment = models.CharField(null=True, default='', max_length=300, blank=True)
    # 入职时间
    # auto_now_add: 自动保存新增一条数据的时间,不需要手动进行赋值
    hire_date = models.DateField(auto_now_add=True)
    # 定义关联属性: 指定员工属于所一个部门, 在表中会生成外键:department_id
    department = models.ForeignKey('Department')

    def __str__(self):
        return self.name

    class Meta:
        # 指定表名
        db_table = 'employee'

        verbose_name = '员工'
        verbose_name_plural = verbose_name  # 去掉复数的s



class TestUser(models.Model):

    name = models.CharField(max_length=20)
    # 头像: 表示把上传的图片保存在 media/user子文件夹中
    avatar = models.ImageField(upload_to='user')

#
# class Teacher(models.Model):
#     """教师:多对多"""
#     name = models.CharField(max_length=20)
#     # 多对多关联属性
#     classes = models.ManyToManyField('Class')
#
#
# class Class(models.Model):
#     """班级类"""
#     name = models.CharField(max_length=20)
#
#     # # 多对多关联属性
#     # teachers = models.ManyToManyField('Teacher')


