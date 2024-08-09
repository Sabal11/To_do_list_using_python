from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from  .models import task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class Tasklist(LoginRequiredMixin, ListView):
    model = task
    context_object_name = 'task'
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task']=context['task'].filter(user = self.request.user)
        context['count']= context['task'].filter(complete=False).count()
        return context
    

class Taskdetail(LoginRequiredMixin, DetailView):
    model = task

class TaskCreate(LoginRequiredMixin, CreateView):
    model = task
    fields = ['title', 'description','complete']
    success_url = reverse_lazy('Task')
    template_name = 'todo/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class Taskupdate(LoginRequiredMixin, UpdateView):
    model = task
    fields = "__all__"
    success_url = reverse_lazy('Task')
    template_name = 'todo/update.html'

class Taskdelete(LoginRequiredMixin, DeleteView):
    model = task
    template_name = 'todo/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('Task')

class Login(LoginView):
    template_name = 'todo/login.html'
    fields = "__all__"
    redirect_authentication = False

    def get_success_url(self):
        return reverse_lazy('Task')

class Register(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('Task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)
    









     



