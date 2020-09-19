from django.urls import path
from . import views

app_name = 'scenes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.scene_create_view, name='scene_create_view')
]