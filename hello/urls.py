from django.urls import path
from hello import views

urlpatterns = [
    path("django", views.home, name="home"),
    path("boris", views.boris, name="b1"),
    #path("hello/<name>", views.hello_there, name="there"),
    path("hello/<name>", views.hello_there, name="there"),
]