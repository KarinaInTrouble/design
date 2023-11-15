from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login

# Create your views here.

def index(request):
    executors = Executor.objects.all()[:3]
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FeedbackForm()

    return render(request, 'index.html', {'executors': executors, 'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def client(request):
    return render(request, 'client.html')

def manager(request):
    return render(request, 'manager.html')