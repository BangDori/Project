from django.urls import path
from . import views

NAME = 'APP'
urlpatterns = [
    path('', views.index, name='app'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='reigster'),
    path('board/', views.board, name='board'),
]