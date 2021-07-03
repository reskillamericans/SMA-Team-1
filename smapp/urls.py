from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('register/', views.register, name='register'),
    path('user_detail/', views.user_detail, name='user_detail')
]