from django.urls import path
from .views import *

urlpatterns = [
    path('', TasksHome.as_view(), name= 'home'),
    path('complete/<int:task_id>/', complete, name='task-complete'),
    path('delete/<int:task_id>/', delete, name='delete-task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('task-create', TaskCreateView.as_view(), name='task-create'),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='api-task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='api-task-rud'),
]