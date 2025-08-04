from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'  # Specify the template to use for the login view
    fields = '__all__'  # This will include all fields in the form
    redirect_authenticated_user = True  # Redirect authenticated users to the home page

    def get_success_url(self):
        return reverse_lazy('task-list')  # Redirect to the task list after successful login
    
    tem

# Create your views here.
class TskList(ListView):
    # This view will render the task list page
   model = Task 
   context_object_name = 'tasks'  # This will be the name of the variable in the template

class TaskDetail(DetailView):
    # This view will render the task detail page
    model = Task
    context_object_name = 'task'  # This will be the name of the variable in the template   
    template_name = 'base/task.html'  # Specify the template to use for this view

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'  # This will include all fields in the form
    success_url = reverse_lazy('task-list')  # Redirect to the task list after successful creation

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'  # This will include all fields in the form
    success_url = reverse_lazy('task-list')  # Redirect to the task list after successful update

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'  # This will be the name of the variable in the template
    success_url = reverse_lazy('task-list')  # Redirect to the task list after successful deletion
    template_name = 'base/task_confirm_delete.html'  # Specify the template to use for this view