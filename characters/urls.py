from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create-character'),
    path('<int:pk>/', views.DetailView.as_view(), name='show-character'),
    path('<int:pk>/edit', views.UpdateView.as_view(), name='edit-character'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete-character'),
]