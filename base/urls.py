from django.urls import path
from .views import TskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'), # URL for login view
    path('register/', RegisterPage.as_view(), name = 'register'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('', TskList.as_view(), name='task-list'),  # URL for the task list view
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'), 
    path('task-create/', TaskCreate.as_view(), name='task-create'), # URL for the task detail view
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),  # URL for the task update view
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),  # URL for the task delete view   
]