from django.urls import path
from .views import index, register, user_detail, login, forgot_password, follow_user
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path('', index, name ='index'),
    path('register/',register, name='register'),
    path('user_detail/',user_detail, name='user_detail'),
    path('login/',login, name='login'),
    path('forgot_password/',forgot_password, name='forgot_password'),
    path('password_reset/<token>/',password_reset, name='password_reset'),
    path('follow/str:user_id>/',follow_user, name = 'follow_user'),

]