from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from website.models import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from website.forms import *

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def copyright(request):
    return render(request, "website/copyright.html")

def projects(request):
    projects = Project.objects.all()
    return render(request, "website/projects.html", {'projects': projects})

def project(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, "website/show_project.html", {'project': project})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('website:projects'))
    else:
        form = ProjectForm()
    return render(request, "website/add_project.html", {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('website:index'))
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, "website/login.html")
