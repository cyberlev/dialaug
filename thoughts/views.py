from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse

from .models import Thought
from .forms import ModelThoughtCreateForm

class IndexView(generic.ListView):
    template_name = 'thoughts/index.html'
    context_object_name = "thoughts"

    def get_queryset(self):
        return Thought.objects.all()

class DetailView(generic.DetailView):
    model = Thought
    template_name = 'thoughts/show_thought.html'

    def get_queryset(self):
        return Thought.objects.all()

class CreateView(generic.CreateView):
    model = Thought
    template_name = 'thoughts/create_thought.html'
    form_class = ModelThoughtCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class UpdateView(generic.UpdateView):
    model = Thought
    template_name = 'thoughts/create_thought.html'
    form_class = ModelThoughtCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteView(generic.DeleteView):
    model = Thought
    template_name = 'thoughts/delete_thought.html'

    def get_queryset(self):
        return Thought.objects.all()
    
    def get_success_url(self):
        return reverse('thoughts:index')