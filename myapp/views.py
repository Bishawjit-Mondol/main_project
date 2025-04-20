from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Hello, world!")


def profile(request):
    return HttpResponse("This is the profile page.")


def dashboard(request):
    return HttpResponse("This is the dashboard page.")


def about(request):
    return render(request, 'about.html', {'title': 'About Us'})