from django.shortcuts import render
from django.views import generic

from .models import Character

from .forms import CharacterCreateForm, RawCharacterCreateForm

class IndexView(generic.ListView):
    template_name = 'characters/index.html'
    context_object_name = "characters"

    def get_queryset(self):
        return Character.objects.all()

class CreateView(generic.CreateView):
    model = Character
    template_name = 'characters/create_character.html'
    form_class = CharacterCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

def character_create_view(request):
    form = CharacterCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = CharacterCreateForm()

    context = {
        'form': form
    }

    return render(request, "characters/character_create.html", context)

def raw_character_create_view(request):
    form = RawCharacterCreateForm(request.POST)

    context = {
        "form": form,
    }

    return render(request, "characters/character_create.html", context)