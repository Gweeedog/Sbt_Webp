from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("tasks/", views.tasks, name="tasks"),
    path("orders/", views.orders, name="orders"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("logout/", views.logout_view, name="logout"),
    path("store/", views.store, name="store"),
    path("task_request/", views.task_request, name="task_request"),
    path("order_request/", views.order_request, name="order_request")

]