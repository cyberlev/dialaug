from django.urls import path

from . import views

app_name = 'lines'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create_view, name='create-line'),
    path('<int:pk>/', views.DetailView.as_view(), name='show-line'),
    path('<int:pk>/edit/', views.UpdateView.as_view(), name='edit-line'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete-line'),
]
