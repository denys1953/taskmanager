from django.urls import path
from .views import *

urlpatterns = [
    path('', TasksHome.as_view(), name= 'home'),
    path('complete/<int:task_id>/', complete, name='task-complete'),
    path('delete/<int:task_id>/', delete, name='delete-task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('task-create', TaskCreateView.as_view(), name='task-create')
]