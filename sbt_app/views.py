from django.shortcuts import render, redirect
from .models import task, order, customer, sake_item, order_metadata
from .forms import RegisterForm, TaskRequestForm, OrderRequestForm, AddCustomerForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
import datetime
from zoneinfo import ZoneInfo


# Create your views here.
def home(request):
    return render(request, "home.html")

def is_member(user):
    return user.groups.filter(name='member').exists()

@login_required(login_url="/login")
@user_passes_test(is_member)
def tasks(request):
    items = task.objects.all()
    user_tasks = task.objects.filter(target=request.user, completed=False)
    completed_tasks = task.objects.filter(target=request.user, completed=True)
    
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

    return render(request, "tasks.html", {"tasks": items, "user_tasks": user_tasks, "completed_tasks":completed_tasks})

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
@user_passes_test(is_member)
def task_request(request):
    if request.method == "POST":
        form = TaskRequestForm(request.POST)
        if form.is_valid():
            newtask = task()
            newtask.submission_date = datetime.datetime.now(tz=ZoneInfo("Europe/Rome"))
            newtask.author = request.user
            usr_num = form.cleaned_data["incaricato"]
            newtask.target = form.choices[int(usr_num)][1]
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

@login_required(login_url="/login")
@user_passes_test(is_member)
def add_customer(request):
    if request.method == "POST":
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            new_customer = customer()
            new_customer.name = form.cleaned_data["name"]
            new_customer.code = form.cleaned_data["codice"]
            new_customer.address = form.cleaned_data["address"]
            new_customer.mail_contact = form.cleaned_data["email"]
            new_customer.phone_number = form.cleaned_data["numero_di_telefono"]
            new_customer.billing_name = form.cleaned_data["billing_name"]
            new_customer.billing_address = form.cleaned_data["billing_address"]
            new_customer.piva = form.cleaned_data["piva"]
            new_customer.cf = form.cleaned_data["cf"]
            new_customer.pec = form.cleaned_data["pec"]
            new_customer.codice_univoco = form.cleaned_data["codice_univoco"]
            new_customer.notes = form.cleaned_data["note"]
            new_customer.save()
            return redirect("add_customer")
    else:
        form = AddCustomerForm()
    return render(request, "add_customer.html", {"form": form})


@login_required(login_url="/login")
@user_passes_test(is_member)
def orders(request):
    items = order.objects.all()
    return render(request, "orders.html", {"orders": items})


@login_required(login_url="/login")
@user_passes_test(is_member)
def order_request(request):
    customers = customer.objects.all()
    sake_list = sake_item.objects.all()
    metadata = order_metadata()
    if request.method == "POST":
        item_list = request.POST.get("add-button")
        metadata.selected_customer = request.POST.get("selected_customer")
        
        form = OrderRequestForm(request.POST)
        if item_list:
            contents = request.POST.get("order_contents")
            newcont = request.POST.get("item_name")+"   x "+request.POST.get("item_qty")
            if contents != None:
                contents += "\n"
            contents += newcont
            metadata.contents = contents
            form = OrderRequestForm()
        elif form.is_valid():
            """
            new_order = order()
            new_order.author = request.user
            new_order.destination = customers.get(name=str(request.POST.get("selected_customer")))
            new_order.delivery = form.cleaned_data["data_di_consegna_prevista"]
            new_order.code = form.cleaned_data["codice"]
            new_order.contents = form.cleaned_data["contenuto"]
            new_order.save()
            return redirect("orders")
            """
            print("form is valid")
    else:
        form = OrderRequestForm()
    return render(request, "order_request.html", {"form": form, "customers": customers, "metadata": metadata, "sake_list":sake_list})
