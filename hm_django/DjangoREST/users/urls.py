from django.conf.urls import url
from rest_framework.routers import SimpleRouter, DefaultRouter

from users import views
#from users.views import DepartmentViewSet, EmployeeViewSet

urlpatterns = [

    url(r'^index$', views.index),

    url(r'^department$', views.department),
    url(r'^employee$', views.employee),
]