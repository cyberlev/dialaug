from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Scene

from .forms import SceneCreateForm, AddLineForm

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

    def post(self, request, *args, **kwargs):
        form = AddLineForm(request.POST)
        scene = self.get_object()

        
        if form.is_valid():
            scene.line_set.create(text=form.cleaned_data['text'], character=scene.characters.get(pk=form.cleaned_data['character']), scene=scene)

            return HttpResponseRedirect(scene.get_absolute_url())
        else:
            return HttpResponseRedirect(scene.get_absolute_url())


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

def characters_view(request, pk):
    scene = get_object_or_404(Scene, pk=pk)
    characters = scene.characters.all()
    
    context = {
        'scene': scene,
        'characters': characters
    }

    return render(request, 'scenes/characters.html', context)