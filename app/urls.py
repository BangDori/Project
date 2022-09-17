from django.urls import path
from . import views

NAME = 'APP'
urlpatterns = [
    path('', views.goIndex, name='go'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index/dabang/', views.dabang, name='dabang'),
    path('index/succession/', views.succession, name='succession'),
    path('index/essentials/', views.essentials, name='essentials'),
    path('index/group/', views.group, name='group'),
    path('index/board/', views.board, name='board'),
    path('index/notice/', views.notice, name='notice'),
    path('index/contact/', views.contact, name='contact'),
    path('index/write/', views.write, name='write'),
    path('findID/', views.fintID, name='findID'),
]