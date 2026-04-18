from django.http import HttpResponse
from .models import Task
from django.shortcuts import render, redirect
# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
    return HttpResponse('the form is submitted')
