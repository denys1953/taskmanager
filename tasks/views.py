from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, DetailView, CreateView
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskUpdateForm, TaskCreateForm
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TasksHome(ListView):
    model = Task
    template_name = "task-list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all()

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task-detail.html'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update-task.html'
    form_class = TaskUpdateForm
    success_url = reverse_lazy('home')

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task-create.html'
    form_class = TaskCreateForm
    success_url = reverse_lazy('home')

def complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()

    return redirect('home')

def delete(request, task_id):
    Task.objects.get(pk=task_id).delete()

    return redirect('home')


def register(request):
    pass

def login(request):
    pass

