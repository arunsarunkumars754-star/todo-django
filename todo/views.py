from django.http import HttpResponse
from .models import Task
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
    return HttpResponse('the form is submitted')

def mark_as_done(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    if request.method == 'POST': 
        task.task = request.POST['task']
        task.save()
        return redirect('home')
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')