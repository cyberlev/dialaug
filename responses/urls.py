from django.urls import path

from . import views

app_name = 'responses'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create-response'),
    path('<int:pk>/', views.DetailView.as_view(), name='show-response'),
    path('<int:pk>/edit', views.UpdateView.as_view(), name='edit-response'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete-response'),
]