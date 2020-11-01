from django.shortcuts import render
from django.utils import timezone
from todos.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by("-added_date")
    context = {
        "todos" : todos
    }
    return render(request, 'todos/index.html', context)

def add_todo(request):
    print(request)
    curr_date = timezone.now()
    curr_todo = request.POST["todo"]
    print(curr_date)
    print(curr_todo)
    todo_item = Todo.objects.create(item=curr_todo, added_date=curr_date)
    print(todo_item)
    print(todo_item.id)
    return HttpResponseRedirect('/')

def delete_todo(request, id):
    print(id)
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect('/')

