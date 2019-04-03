from django.conf.urls import url

from users import views

urlpatterns = [

    url(r'^index$', views.index),

    #url(r'^department$', views.department),
    #url(r'^employee$', views.employee),
]