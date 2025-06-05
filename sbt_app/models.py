from django.db import models
from django.contrib.auth.models import User
import datetime

def get_default_time():
    default_time = datetime.datetime(
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        19, 00
    )
    return default_time

class task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_limit = models.DateTimeField(default = get_default_time(), blank=False, null=False)
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

