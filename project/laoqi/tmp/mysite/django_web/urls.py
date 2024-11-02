from django.urls import path
from django_web.views import views_api

# 在django_web下创建urls.py，配置具体接口的二级目录

urlpatterns = [
    # guest system interface:
    # ex : /api/add_event/
    path('add_event/', views_api.add_event, name='add_event'),
    # ex : /api/get_event_list/
    path('get_event_list/', views_api.get_event_list, name='get_event_list'),
    # ex: /api/add_guest/
    path('add_guest/', views_api.add_guest, name='add_guest'),
    # ex: /api/get_guest_list/
    path('get_guest_list/', views_api.get_guest_list, name='get_guest_list'),
    # ex: /api/user_sign/
    path('user_sign/', views_api.user_sign, name='user_sign'),
]