from django.contrib import admin
from .models import task, sake_item, order, customer

admin.site.register(task)
admin.site.register(sake_item)
admin.site.register(order)
admin.site.register(customer)