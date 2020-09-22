from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import *
from django.contrib import *
from .forms import *
from .models import *
from .decorators import *

# Create your views here.


@login_required(login_url='login')
def home(request):

    task_info = request.user.taskinfo.all()
    context = {'taskInfo': task_info}
    return render(request, 'main/home.html', context)


@unauthenticatedUser
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')
    context = {}
    return render(request, 'main/forms/login.html', context)


@unauthenticatedUser
def registerPage(request):
    registerForm = createUserForm()
    if request.method == 'POST':
        registerForm = createUserForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect('login')

    context = {'registerForm': registerForm}
    return render(request, 'main/forms/register.html', context)


@login_required(login_url='login')
def createTask(request):
    createTask_form = createTaskForm()
    if request.method == 'POST':
        createTask_form = createTaskForm(request.POST)
        if createTask_form.is_valid():
            form = createTask_form.save(False)
            form.user = request.user
            form.save()
            return redirect('home')

    context = {'createTaskForm': createTask_form}
    return render(request, 'main/createTask.html', context)


@login_required(login_url='login')
def deleteTask(request, tid):
    delete_task = TaskInfo.objects.get(id=tid)
    if request.method == 'POST':
        delete_task.delete()
        return redirect('home')

    context = {'task': delete_task}
    return render(request, 'main/delete.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('/login')
