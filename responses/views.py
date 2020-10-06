from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse

from .models import Response
from .forms import ResponseCreateForm 

class IndexView(generic.ListView):
    template_name = 'responses/index.html'
    context_object_name = "responses"

    def get_queryset(self):
        return Response.objects.all()

class DetailView(generic.DetailView):
    model = Response
    template_name = 'responses/show_response.html'

    def get_queryset(self):
        return Response.objects.all()

class UpdateView(generic.UpdateView):
    model = Response
    template_name = 'responses/create_response.html'
    form_class = ResponseCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class CreateView(generic.CreateView):
    model = Response
    template_name = 'responses/create_response.html'
    form_class = ResponseCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteView(generic.DeleteView):
    model = Response
    template_name = 'responses/delete_response.html'

    def get_queryset(self):
        return Response.objects.all()
    
    def get_success_url(self):
        return reverse('responses:index')