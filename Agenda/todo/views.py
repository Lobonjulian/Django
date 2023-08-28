from django.shortcuts import render, redirect
from .models import Todo
from  .forms import TodoForm
from django.contrib import messages

# para tener un buscardor de busqueda en la pagina
def index(request):
    todos = Todo.objects.filter(titulo__contains=request.GET.get('search', ''))
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)

def view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todos': todo
    }
    return render(request, 'todo/view.html')

def edit(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizado')
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)

def create(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'todo/create.html', context) 
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo')
