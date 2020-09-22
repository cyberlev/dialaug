from django.urls import path
from . import views

app_name = 'scenes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create-scene'),
    path('<int:pk>/', views.DetailView.as_view(), name='show-scene'),
    path('<int:pk>/edit', views.UpdateView.as_view(), name='edit-scene'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete-scene'),
    path('<int:pk>/characters', views.characters_view, name='characters-scene'),
]