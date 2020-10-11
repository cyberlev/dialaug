from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Line
from .forms import LineCreateForm, ModelLineCreateForm, AddResponseForm

from responses.forms import ResponseCreateForm

class IndexView(generic.ListView):
    template_name = 'lines/index.html'
    context_object_name = "lines"

    def get_queryset(self):
        return Line.objects.all()

class DetailView(generic.DetailView):
    model = Line
    template_name = 'lines/show_line.html'

    def get_queryset(self):
        return Line.objects.all()

    def post(self, request, *args, **kwargs):
        form = AddResponseForm(request.POST)
        self.object = self.get_object()

        if form.is_valid():
            # <process form cleaned data>
            self.object.response_set.create(text=form.cleaned_data['text'])
            return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            return HttpResponseRedirect(self.object.get_absolute_url())


    
class UpdateView(generic.UpdateView):
    model = Line
    template_name = 'lines/create_line.html'
    form_class = ModelLineCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class CreateView(generic.CreateView):
    model = Line
    template_name = 'lines/create_line.html'
    form_class = ModelLineCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteView(generic.DeleteView):
    model = Line
    template_name = 'lines/delete_line.html'

    def get_queryset(self):
        return Line.objects.all()
    
    def get_success_url(self):
        return reverse('lines:index')

def add_response(request):
    if request.method == 'POST':
        line_id = request.POST.get('line_id')
        line = Line.objects.get(pk=line_id)

        print(line.text) 