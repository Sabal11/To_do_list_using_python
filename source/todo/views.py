from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from  .models import task
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class Tasklist(ListView):
    model = task
    context_object_name = 'task'
    template_name = 'todo/index.html'

class Taskdetail(DetailView):
    model = task

class TaskCreate(CreateView):
    model = task
    fields = "__all__"
    success_url = reverse_lazy('Task')
    template_name = 'todo/form.html'

class Taskupdate(UpdateView):
    model = task
    fields = "__all__"
    success_url = reverse_lazy('Task')
    template_name = 'todo/update.html'


     



