from django.shortcuts import render, redirect
from .models import task
from .forms import RegisterForm, TaskRequestForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime
from zoneinfo import ZoneInfo


# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required(login_url="/login")
def tasks(request):
    items = task.objects.all()
    
    if request.method == "POST":
        delete_id = request.POST.get("delete_id")
        complete_id = request.POST.get("complete_id")

        if delete_id:
            mytask = task.objects.filter(id=delete_id).first()
            if mytask :
                mytask.delete()
        elif complete_id:
            mytask = task.objects.filter(id=complete_id).first()
            if mytask :
                mytask.datetime_limit = datetime.datetime.now(tz=ZoneInfo("Europe/Rome"))
                mytask.completed = True
                mytask.save()

    return render(request, "tasks.html", {"tasks": items})

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, 'registration/sign-up.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

def store(request):
    return render(request, "store.html")

@login_required(login_url="/login")
def task_request(request):
    if request.method == "POST":
        form = TaskRequestForm(request.POST)
        if form.is_valid():
            newtask = task()
            newtask.submission_date = datetime.datetime.now(tz=ZoneInfo("Europe/Rome"))
            newtask.author = request.user
            newtask.target = form.cleaned_data["target"]
            newtask.title = form.cleaned_data["title"]
            date_value = form.cleaned_data["data_limite"]
            time_value = form.cleaned_data["orario_limite"]
            newtask.datetime_limit = datetime.datetime(
                year=date_value.year,
                month=date_value.month,
                day=date_value.day,
                hour=time_value.hour,
                minute=time_value.minute,
                second=00
            )
            newtask.save()
            return redirect("tasks")
    else:
        form = TaskRequestForm()
    return render(request, "task_request.html", {"form": form})