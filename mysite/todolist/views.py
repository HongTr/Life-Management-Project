from django.contrib import messages
from django.shortcuts import redirect, render
from todolist.models import ToDoLists

# Create your views here.
def todolist(response, list_name):
    user_todolist = ToDoLists.objects.filter(user_id = response.user.id)
    now_todolist = ToDoLists.objects.get(name = list_name)
    context = {
        "user_todolist": user_todolist,
        "now_todolist": now_todolist
    }
    return render(response, "todolist/todolist.html", context)

def create_new_todolist(response, list_name):
    new_todolist_name = ToDoLists.ListNameGenerator(response)
    if new_todolist_name != None:
        new_todolist = ToDoLists(user_id = response.user.id, name = new_todolist_name)
        new_todolist.save()
        return redirect(f"/todolist_{new_todolist_name}")
    else:
        return redirect(f"/todolist_{list_name}")

def delete_todolist(response, list_name):
    delete_todolist = ToDoLists.objects.get(user_id = response.user.id, name = list_name)
    delete_todolist.delete()
    return redirect("/deleted_todolist")

def deleted_todolist(response):
    user_todolist = ToDoLists.objects.filter(user_id = response.user.id)
    context = {
        "user_todolist": user_todolist,
    }
    return render(response, "todolist/deleted_todolist.html", context)