from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    User._meta.get_field('username').validators[1].limit_value = 15
    email = forms.EmailField(required=True)
    indirizzo = forms.CharField(max_length=200, required=True)
    numero_di_telefono = forms.CharField(max_length=12, min_length=10, required=False)


    class Meta:
        model = User
        fields = ["username", "email", "indirizzo", "numero_di_telefono", "password1", "password2"]