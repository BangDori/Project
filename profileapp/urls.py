from django.urls import path

from . import views
from .views import ProfileCreateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('view', views.view, name='view')
]