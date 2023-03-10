from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Tarefa
from .forms import Taskform
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def tasksList(request):
    usuario = request.user
    search = request.GET.get('search')
    filtro = request.GET.get('filter')

    if search:
        tasks = Tarefa.objects.filter(usuario=usuario, titulo__icontains=search)
    elif filtro:
        tasks = Tarefa.objects.filter(usuario=usuario, done=filtro)
    else:

        tasks_list = Tarefa.objects.filter(usuario=usuario).order_by('-data_criacao')

        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'lista.html', {'tasks': tasks})
@login_required(login_url='/login/')
def taskView(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    return render(request, 'tasks.html', {'task': task})

@login_required(login_url='/login/')
def newTask(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.usuario = request.user
            task.save()
            return redirect('/')
    else:
        form = Taskform()
        return render(request, 'addtask.html', {'form':form})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def deleteTask(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    task.delete()
    return redirect('/')

@login_required(login_url='/login/')
def change_status(request, id):
    task = get_object_or_404(Tarefa, pk=id)

    if task.done == 'doing':
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()
    return redirect('/')