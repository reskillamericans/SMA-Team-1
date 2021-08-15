from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='auth'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
]