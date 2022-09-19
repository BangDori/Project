from django.urls import path
from . import views

NAME = 'APP'
urlpatterns = [
    path('', views.goIndex, name='go'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('index/dabang/', views.dabang, name='dabang'),
    path('index/succession/', views.succession, name='succession'),
    path('index/essentials/', views.essentials, name='essentials'),
    path('index/group/', views.group, name='group'),
    path('index/board/', views.board, name='board'),
    path('index/notice/', views.notice, name='notice'),
    path('index/contact/', views.contact, name='contact'),
    path('index/write/', views.write, name='write'),
    path('findID/', views.findID, name='findID'),
    path('findPW1/', views.findPW1, name='findPW1'),
    path('findPW1/findPW2/', views.findPW2, name='findPW2'),
]