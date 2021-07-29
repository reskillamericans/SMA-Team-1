from django.urls import path
from .views import register, login, forgot_password, password_reset
from smapp.views import index

app_name = "accounts"

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('user_detail/', user_detail, name='user_detail'),
    path('login/', login, name='login'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('password_reset/<token>/', password_reset, name='password_reset'),
]