from django.shortcuts import render, redirect
from tarefas.models import Tarefas


def index(request):

    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas/index.html', {"Tarefas": tarefas})
    # return HttpResponse("!")


def create(request):
    return render(request, 'tarefas/c.html')



def save(request):
    description = request.POST.get("description")
    owner = request.POST.get("owner")
    duedate = request.POST.get("duedate")
    isdone = request.POST.get("isdone")
    Tarefas.objects.create(description=description, owner=owner, duedate=duedate, isdone=isdone)
    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas/index.html', {"Tarefas": tarefas})


def update(request, id):
    tarefa = Tarefas.objects.get(id=id)
    return render(request, 'tarefas/u.html', {"Tarefa": tarefa})


def save_update(request, id):
    description = request.POST.get("description")
    owner = request.POST.get("owner")
    duedate = request.POST.get("duedate")
    isdone = request.POST.get("isdone")

    tarefas = Tarefas.objects.get(id=id)
    tarefas.description = description
    tarefas.owner = owner
    tarefas.duedate = duedate
    tarefas.isdone = isdone
    tarefas.save()
    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas/index.html', {"tarefas": tarefas})


def delete(request, id):
    tarefa = Tarefas.objects.get(id=id)
    return render(request, 'tarefas/d.html', {"Tarefa": tarefa})


def save_delete(request, id):
    tarefas = Tarefas.objects.get(id=id)
    tarefas.delete()
    tarefas = Tarefas.objects.all()
    return redirect(index)

