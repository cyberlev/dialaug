from django.shortcuts import render
from django.views import generic
from django.urls import reverse

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

class DetailView(generic.DetailView):
    model = Character
    template_name = 'characters/show_character.html'

    def get_queryset(self):
        return Character.objects.all()

class UpdateView(generic.UpdateView):
    model = Character
    template_name = 'characters/create_character.html'
    form_class = CharacterCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteView(generic.DeleteView):
    model = Character
    template_name = 'characters/delete_character.html'

    def get_queryset(self):
        return Character.objects.all()

    def get_success_url(self):
        return reverse('characters:index')