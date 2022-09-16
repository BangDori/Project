from django.urls import path
from . import views

NAME = 'APP'
urlpatterns = [
    path('', views.index, name='app'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='reigster'),
    path('dabang/', views.dabang, name='dabang'),
    path('succession/', views.succession, name='succession'),
    path('essentials/', views.essentials, name='essentials'),
    path('group/', views.group, name='group'),
    path('board/', views.board, name='board'),
    path('notice/', views.notice, name='notice'),
    path('contact/', views.contact, name='contact'),
    path('write/', views.write, name='write'),
]