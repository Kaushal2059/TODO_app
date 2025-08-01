from django.urls import path
from .views import TskList, TaskDetail

urlpatterns = [ 
    path('', TskList.as_view(), name='task-list'),  # URL for the task list view
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),  # URL for the task detail view
]