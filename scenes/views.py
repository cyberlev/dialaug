from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from .models import Scene

from .forms import SceneCreateForm

class IndexView(generic.ListView):
    template_name = 'scenes/index.html'
    context_object_name = "scenes"

    def get_queryset(self):
        return Scene.objects.all()

class CreateView(generic.CreateView):
    model = Scene
    template_name = 'scenes/create_scene.html'
    form_class = SceneCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class DetailView(generic.DetailView):
    model = Scene
    template_name = 'scenes/show_scene.html'

    def get_queryset(self):
        return Scene.objects.all()

class UpdateView(generic.UpdateView):
    model = Scene
    template_name = 'scenes/create_scene.html'
    form_class = SceneCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteView(generic.DeleteView):
    model = Scene
    template_name = 'scenes/delete_scene.html'

    def get_queryset(self):
        return Scene.objects.all()
    
    def get_success_url(self):
        return reverse('scenes:index')