from django.urls import reverse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime

#def home(request):
#    return HttpResponse("Hello, Django!")

def boris(request):
    return HttpResponse("Hello, Boris!")


def hello_there(request, name):
    return render(request, 'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")