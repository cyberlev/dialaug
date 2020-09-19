from django.shortcuts import render
from django.views import generic

from .models import Scene

from .forms import SceneCreateForm

class IndexView(generic.ListView):
    template_name = 'scenes/index.html'
    context_object_name = "scenes"

    def get_queryset(self):
        """Return the last five published questions."""

        return Scene.objects.all()

def scene_create_view(request):
    form = SceneCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = SceneCreateForm()

    context = {
        'form': form
    }

    return render(request, "scenes/scene_create.html", context)