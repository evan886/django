"""django01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from users import views

# users/index
# index
urlpatterns = [

    # 127.0.0.1:8000/users/index
    # 配置路由地址
    # 参数1: 匹配url的正则表达式
    # 参数2: 匹配成功后执行的视图
    # url(r'^users/index$', views.index)

    # url(r'^index$', views.index),

    # 包含users模块下的urls.py文件
    # url(r'^users/', include('users.urls'))

    # 任意的字符串与^都可以匹配成功
    url(r'^admin/', admin.site.urls),

    url(r'^', include('users.urls')),
]