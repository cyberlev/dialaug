from django.urls import path
from . import views

app_name = 'thoughts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='show-thought'),
    path('create/', views.CreateView.as_view(), name='create-thought'),
    path('<int:pk>/edit/', views.UpdateView.as_view(), name='edit-thought'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete-thought')
]