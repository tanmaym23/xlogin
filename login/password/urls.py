# from django.conf.urls import urls
from django.urls import path,include
from password import views

app_name='password'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login',views.user_login,name='login')
]