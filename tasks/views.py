from django.shortcuts import render
from django.http import HttpResponse

def TasksHome(request):
    return render(request, "base.html")