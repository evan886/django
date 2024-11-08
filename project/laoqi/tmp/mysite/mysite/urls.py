"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path, include
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from api import views


router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

   #api jun 06 2021
   path('api/',include('django_web.urls')),


    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('blog/',include('blog.urls',namespace='blog')),
    #path('account/',include('account.urls',namespace='account')),
    path('account/', include('account.urls', namespace='account')),

    #blog_api 
    #path('articles/',add_article),
    #path('articles/<int:art_id>',modify_article)

    # namespace 是什么来着

]
