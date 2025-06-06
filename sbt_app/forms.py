from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import task, order, customer
from django.forms import ModelForm
from datetime import datetime, date, timedelta

def get_default_delivery_date():
    newdate = datetime.now() + timedelta(days=1, hours=12)
    if newdate.weekday() > 4:
        newdate += timedelta(days= 7 - newdate.weekday())

    delivery_date = newdate
    return delivery_date

class RegisterForm(UserCreationForm):
    User._meta.get_field('username').validators[1].limit_value = 15
    email = forms.EmailField(required=True)
    indirizzo = forms.CharField(max_length=200, required=True)
    numero_di_telefono = forms.CharField(max_length=12, min_length=10, required=False)


    class Meta:
        model = User
        fields = ["username", "email", "indirizzo", "numero_di_telefono", "password1", "password2"]

class TaskRequestForm(ModelForm):
    data_limite = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"}), initial=str(date.today()))
    orario_limite = forms.TimeField(required=True, widget=forms.TimeInput(attrs={"type": "time"}), initial= "19:00")
    i = 0
    usr_list = []
    for usr in User.objects.filter(groups__name='member'):
        usr_list.append((i, usr))
        i += 1
    choices=tuple(usr_list)
    incaricato = forms.ChoiceField(required=True, choices=choices)
    class Meta:
        model = task
        fields = ("title", "data_limite", "orario_limite")
        labels = {
            "title": "Contenuto",
        }


class AddCustomerForm(ModelForm):
    customer_num = customer.objects.all().count()
    codice = forms.IntegerField(initial=customer_num + 1, required=True)
    email = forms.EmailField(max_length=254, required=False)
    numero_di_telefono = forms.CharField(max_length=15, required=True, initial="")
    pec = forms.EmailField(max_length=254, required=False)
    note = forms.CharField(max_length=200, required=False, initial="")
    class Meta:
        model = customer
        fields = ("codice", "name", "address", "email", "numero_di_telefono", "billing_name", "billing_address", "piva", "cf", "pec", "codice_univoco", "note")
        labels = {
            "name": "Nome",
            "address": "Indirizzo",
            "billing_name": "Nome per fatturazione",
            "billing_address": "Indirizzo di fatturazione"
        }


class OrderRequestForm(ModelForm):
    codice = forms.CharField(max_length=5, required=True, initial="G001")
    data_di_consegna_prevista = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"}), initial=str(get_default_delivery_date().date()))
    class Meta:
        model = order
        fields = ("codice", "data_di_consegna_prevista")