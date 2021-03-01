from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def woosal(request):
    return HttpResponse("Hello, Vusal!")

def chalabi(request):
    return HttpResponse("Hello, Chalabi!")

def greet(request, name):
    return render(request, "hello/greet.html", {
       "name":name.capitalize()
    })