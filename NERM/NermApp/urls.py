from django.urls import path
from NermApp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'NermApp'

urlpatterns = [
    path('events', views.events, name='events'),
    path('digitalSet', views.digitalSet, name='digitalSet'),
    path('analogSet', views.analogSet, name='analogSet'),
    path('jobInfo', views.jobInfo, name='jobInfo'),
    path('changeIp', views.changeIp, name='changeIp'),
    path('monitor', views.monitor, name='monitor'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login')
]
