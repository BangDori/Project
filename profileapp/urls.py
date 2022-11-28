from django.urls import path

from . import views
from .views import ProfileCreateView

app_name = 'profileapp'

urlpatterns = [
    # path('create/', ProfileCreateView.as_view(), name='create'),
    path('view', views.view, name='view'),
    path('profile/', ProfileCreateView.as_view(), name='profile'),
    # path('profile/', views.profile),
    path('mypage/', views.mypage),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('mypost/', views.mypost, name='mypost'),
    path('favorites/', views.favorites, name='favorites'),
    path('address/', views.Address.as_view(), name='address'),
    path('corporate/', views.corporate, name='register')
]
