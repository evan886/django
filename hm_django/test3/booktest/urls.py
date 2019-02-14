from django.conf.urls import url
import views
import views1

urlpatterns=[
    url(r'^$',views1.index),
    #url(r'^$', views.index),
    url(r'^(\d+)$',views.detail)
]