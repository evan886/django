from django.conf.urls import url 
# form . import views # from no form 
from . import views

urlpatterns = [
    url(r'^$', views.blog_title,name="blog_title"),
    url(r'(?P<article_id>\d)/$', views.blog_article,name="blog_detail"),
    
]