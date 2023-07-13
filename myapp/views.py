from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.http import HttpResponse

def home(request):
    task = Task.objects.filter(is_completed = False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True)
    # task_undone = Task.objects.filter(is_completed=False)

    context = {
        'task':task,
        'completed_task':completed_task,
        # 'task_undone':task_undone
         }
    return render(request,'home.html',context)

def addtask(request):
    if request.method == "POST":
        addtask = request.POST["addingtask"]
        Task.objects.create(task=addtask)
        return redirect('home')
    
def MarkAsDone(request ,pk):
    taskdone = get_object_or_404(Task,pk=pk)
    taskdone.is_completed = True
    taskdone.save()
    return redirect('home')

def MarkAsUnDone(request,pk):
    taskundone = get_object_or_404(Task,pk=pk)
    taskundone.is_completed= False
    taskundone.save()
    return redirect('home')

def edit(request,pk):
    gettask = get_object_or_404(Task,pk=pk)
    if request.method == "POST":
        new_task = request.POST['updating_task']
        gettask.task = new_task
        gettask.save()
        return redirect(home)
    else:
        context = {
            'gettask':gettask
        }
        print(gettask)
        return render(request,'editpage.html',context)
    
def deletetask(request,pk):
    task =get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect(home)