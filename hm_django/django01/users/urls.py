from django.conf.urls import url

from users import views

# index
urlpatterns = [

    # 参数1: 匹配url的正则表达式
    # 参数2: 匹配成功后执行的视图
    url(r'^index$', views.index),

    # news/1/2
    url(r'^news/(?P<category>\d+)/(?P<page>\d+)$', views.news),

    # 传递参数: 通过查询字符串
    # /news2?category=1&page=2&a=1&a=2
    url(r'^news2$', views.news2),

    # 传递参数: body中的键值对
    # /news3
    url(r'^news3$', views.news3),

    # 传递参数: body中的json
    # /news4
    url(r'^news4$', views.news4),
]