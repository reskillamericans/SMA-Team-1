from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name ='index'),
    path('profile/<str:user_id>', views.profile, name = 'profile'),
    path('follow/<str:user_id>', views.follow_user, name = 'follow'),

]