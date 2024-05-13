from django.shortcuts import render,redirect
 
from apps.todo.models import Todo


def homepage(request):
    todos = Todo.objects.all()
    return render(request,'homepage.html',locals())

def create(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        text = request.POST.get('description')
        todos = Todo.objects.create(title=name,text=text,)
        return redirect('index')
    return render(request,'create.html')

def retrieve(request,pk):
    todos = Todo.objects.get(id=pk)
    return render(request,'detail.html',locals())

def destroy(request,pk):
    if request.method == 'POST':
        todos = Todo.objects.get(id=pk)
        return redirect('index')
    return render(request,'destroy.html',locals())

def update(request,pk,todo_id):
    if request.method == 'POST':
        description = request.POST['text']
        todos = Todo.objects.get(id=pk)
        todos.text = description
        todos.title = __name__
        todos=Todo.objects.get(id=todo_id)
        todos.is_complete=not todos.is_complete
        todos.save()
        return redirect('detail',todos.id)
    return render(request,'update.html')