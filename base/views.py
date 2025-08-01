from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def tsk_list(request):
    # This view will render the task list page
    return HttpResponse('To Do List Page')  