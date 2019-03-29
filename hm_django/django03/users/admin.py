from django.contrib import admin
from users.models import Department, Employee #, TestUser



class DepartmentAdmin(admin.ModelAdmin):
    """后台管理类: 可以指定很多后台管理的配置项"""

    # 指定在管理后台显示哪些字段
    list_display = ['id', 'name', 'create_date',"is_delete"]

    # 每页显示多少条
    list_per_page = 3

    # 显示操作栏
    actions_on_top = True
    actions_on_bottom = True

    # 搜索部门名称 讲义说到models去了
    search_fields = ['name']
    # 编辑关联员工对象
    #inlines = [DepartmentTabularInline, DepartmentStackedInline]

class EmployeeAdmin(admin.ModelAdmin):
    """后台管理类: 可以指定很多后台管理的配置项"""

    # 指定在管理后台显示哪些字段
    list_display = ['id', 'name', 'age','gender',
                    'salary', 'comment', 'hire_date',
                    'department'
                    ]

    list_per_page = 10

    # 显示过滤栏: 按性别和部门过滤
    list_filter = ['gender', 'department']


#用到的class 要放在前面 不然找不到 NameError: name 'DepartmentAdmin' is not defined
# admin.sites.register(Department)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)
# Register your models here.