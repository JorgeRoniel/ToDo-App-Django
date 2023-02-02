from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Tarefa
from .forms import Taskform
from django.core.paginator import Paginator

# Create your views here.
def tasksList(request):

    search = request.GET.get('search')
    if search:
        tasks = Tarefa.objects.filter(titulo__icontains=search)
    else:

        tasks_list = Tarefa.objects.all().order_by('-data_criacao')

        paginator = Paginator(tasks_list, 2)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'lista.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    return render(request, 'tasks.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = Taskform()
        return render(request, 'addtask.html', {'form':form})

def editTask(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'edittask.html', {'form': form, 'task': task})

def deleteTask(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    task.delete()
    return redirect('/')