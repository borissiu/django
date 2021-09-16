from django.urls import path
from polls import views


app_name = 'polls'
urlpatterns = [
    path("", views.polls, name="polls"),
]