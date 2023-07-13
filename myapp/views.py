from django.shortcuts import render,redirect
from .models import Task


def home(request):
    task = Task.objects.filter(is_completed = False).order_by('-updated_at')
    context = {'task':task}
    return render(request,'home.html',context)

def addtask(request):
    if request.method == "POST":
        addtask = request.POST["addingtask"]
        Task.objects.create(task=addtask)
        return redirect('home')

