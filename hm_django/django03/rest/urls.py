'''
查询所有部门  GET     /departments/
新增一个部门  POST    /departments/

查询一个部门  GET     /departments/<pk>/
修改一个部门  PUT     /departments/<pk>/
删除一个部门  DELETE  /departments/<pk>/
'''

from django.conf.urls import url
#from rest_framework.routers import SimpleRouter

from rest import views
#from rest.views import DepartmentViewSet

urlpatterns = [

    # # 列表视图
    url(r'^departments/$', views.DepartmentListView.as_view()),
    # # 详情视图
    url(r'^departments/(\d+)/$', views.DepartmentDetailView.as_view()),
]

# 注册drf路由
#router = SimpleRouter()
#router.register('departments', DepartmentViewSet)
#urlpatterns += router.urls  # 追加路由配置
