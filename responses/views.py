from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from lines.models import Line
from characters.models import Character

from .models import Response
from .forms import ResponseCreateForm, AddConsequenceForm 

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

    def post(self, request, *args, **kwargs):
        form = AddConsequenceForm(request.POST)
        self.object = self.get_object()

        if form.is_valid():
            new_line = Line(text=form.cleaned_data['text'], character=Character.objects.get(pk=form.cleaned_data['character']), scene=self.object.line.scene)
            new_line.save()
            self.object.next_line = new_line
            self.object.save()

            return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            return HttpResponseRedirect(self.object.get_absolute_url())




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