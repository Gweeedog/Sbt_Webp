from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import task
from django.forms import ModelForm
import datetime

class RegisterForm(UserCreationForm):
    User._meta.get_field('username').validators[1].limit_value = 15
    email = forms.EmailField(required=True)
    indirizzo = forms.CharField(max_length=200, required=True)
    numero_di_telefono = forms.CharField(max_length=12, min_length=10, required=False)


    class Meta:
        model = User
        fields = ["username", "email", "indirizzo", "numero_di_telefono", "password1", "password2"]

class TaskRequestForm(ModelForm):
    data_limite = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"}), initial=str(datetime.date.today()))
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