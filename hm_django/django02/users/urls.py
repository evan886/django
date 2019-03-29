from django.conf.urls import url

from users import views

urlpatterns= [
    url(r'^home$', views.index, name='index'),

    # /resp
    url(r'^resp$', views.resp),

    url(r'^set_cookie$', views.set_cookie),
    url(r'^get_cookie$', views.get_cookie),

    # /set_session
    url(r'^set_session$', views.set_session),
    # /get_session
    url(r'^get_session$', views.get_session),

    #post(发帖)
    #显示发帖界面 /post
    url(r'^post$', views.post),
    # # 执行发帖操作
    #url(r'^do_post$', views.do_post),

    # 类视图路由配置: /post2
    url(r'^post2$', views.PostView.as_view()),


]

#keyword

