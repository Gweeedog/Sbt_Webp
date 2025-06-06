from django.db import models
from django.contrib.auth.models import User


class task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_limit = models.DateTimeField(blank=False, null=False)
    submission_date = models.DateTimeField(auto_now_add=True, editable=False)

class sake_item(models.Model):
    name = models.CharField(max_length=80)
    maker_name = models.CharField(max_length=50)
    class_type = models.CharField(max_length=50)
    region = models.CharField(max_length=20)
    volume = models.IntegerField()
    jp_code = models.IntegerField()
    it_code = models.IntegerField()
    comment = models.CharField(max_length=200)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    stock = models.IntegerField()
    priority = models.IntegerField()
    stock = models.IntegerField()
    production = models.CharField(max_length=20, default="sokujo moto")
    koji = models.CharField(max_length=20, default="giallo")


class customer(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    address = models.CharField(max_length=100)
    mail_contact = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    billing_name = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=100)
    piva = models.CharField(max_length=20)
    cf = models.CharField(max_length=20)
    pec = models.EmailField(max_length=254)
    codice_univoco = models.CharField(max_length=10)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class order(models.Model):
    code = models.CharField(max_length=5, default=" ")
    destination = models.ForeignKey(customer, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery = models.DateTimeField(blank=False, null=False)
    def __str__(self):
        return self.code
