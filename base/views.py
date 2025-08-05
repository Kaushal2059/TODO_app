from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'  # Specify the template to use for the login view
    fields = '__all__'  # This will include all fields in the form
    redirect_authenticated_user = True  # Redirect authenticated users to the home page

    def get_success_url(self):
        return reverse_lazy('task-list')  # Redirect to the task list after successful login

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')
        return super(RegisterPage, self).get(*args, **kwargs)

class TskList(LoginRequiredMixin, ListView):
    # This view will render the task list page
   model = Task 
   context_object_name = 'tasks'  # This will be the name of the variable in the template

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['tasks'] = context['tasks'].filter(user=self.request.user)
       context['count'] = context['tasks'].filter(completed=False).count()

       search_input = self.request.GET.get('search-area') or ''
       if search_input:
           context['tasks'] = context['tasks'].filter(
               title__icontains = search_input)
           
       context['search_input'] = search_input
           
       return context

class TaskDetail(LoginRequiredMixin, DetailView):
    # This view will render the task detail page
    model = Task
    context_object_name = 'task'  # This will be the name of the variable in the template   
    template_name = 'base/task.html'  # Specify the template to use for this view

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']  # This will include all fields in the form
    success_url = reverse_lazy('task-list')  # Redirect to the task list after successful creation

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']  # This will include all fields in the form
    success_url = reverse_lazy('task-list')  # Redirect to the task list after successful update

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'  # This will be the name of the variable in the template
    success_url = reverse_lazy('task-list')  # Redirect to the task list after successful deletion
    template_name = 'base/task_confirm_delete.html'  # Specify the template to use for this view