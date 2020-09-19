from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.character_create_view, name='character_create_view'),
    path('raw-create/', views.raw_character_create_view, name='raw_character_create_view')
]