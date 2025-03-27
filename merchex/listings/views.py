from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello, Django!</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1>")

def listings(request):
    return HttpResponse("<h1>Listings</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1>")