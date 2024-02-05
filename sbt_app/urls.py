from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("tasks/", views.tasks, name="tasks"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("logout/", views.logout_view, name="logout"),
    path("store/", views.store, name="store")

]