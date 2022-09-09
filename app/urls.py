from django.urls import path
from . import views

NAME = 'APP'
urlpatterns = [
    path('', views.index, name='app'),
    path('login/', views.login, name='login'),
]