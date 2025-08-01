from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

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