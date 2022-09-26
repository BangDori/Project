from django.urls import path
from . import views

NAME = 'APP'
urlpatterns = [
    path('', views.goIndex, name='go'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('board/<str:name>/', views.board, name='board'),
    path('board/<str:name>/<int:pk>', views.article, name='article'),
    path('board/<str:name>/write', views.write, name='write'),
    path('findID/', views.findID, name='findID'),
    path('findID/sms', views.SMS),
    path('findID/sms/send', views.SmsSendView.as_view()),
    path('findID/sms/auth',views.SmsVerifyView.as_view()),
    path('findPW1/', views.findPW1, name='findPW1'),
    path('findPW1/findPW2/', views.findPW2, name='findPW2'),
]
