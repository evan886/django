from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'image_code/(?P<image_code_id>.+)/$', views.ImageCodeView.as_view()),
    #url(r'sms_code/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),
]