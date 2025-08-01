from django.urls import path
from . import views

urlspatterns = [ 
    path('', views.tsk_list, name='task-list'),  # URL for the task list view

]