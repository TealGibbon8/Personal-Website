from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from website.models import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def copyright(request):
    return render(request, "website/copyright.html")

