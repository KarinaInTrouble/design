from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

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

def feedback_list(request):
    feedback_items = Feedback.objects.all().order_by('-timestamp')
    paginator = Paginator(feedback_items, 5)
    page = request.GET.get('page')
    
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        feedbacks = paginator.page(1)
    except EmptyPage:
        feedbacks = paginator.page(paginator.num_pages)
    
    return render(request, 'feedback.html', {'feedbacks': feedbacks})

def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    feedback.delete()
    return redirect('feedback')

def executors(request):
    execs = Executor.objects.all()
    if 'search' in request.GET:
        search_query = request.GET.get('search')
        execs = execs.filter(Q(fullname__icontains=search_query))

    if request.method == 'POST':
        form = ExecutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('executors')
    else:
        form = ExecutorForm()
    return render(request, 'executors.html', {'execs': execs, 'form': form})

def delete_executor(request, pk):
    executor = get_object_or_404(Executor, pk=pk)
    executor.delete()
    return redirect('executors')  # Замените 'list_executors' на URL вашего списка исполнителей

def edit_executor(request, pk):
    executor = get_object_or_404(Executor, pk=pk)

    if request.method == 'POST':
        form = ExecutorForm(request.POST, instance=executor)
        if form.is_valid():
            form.save()
            return redirect('executors')
    else:
        form = ExecutorForm(instance=executor)

    return render(request, 'edit_executor.html', {'form': form, 'executor': executor})





def requests(request):
    reqs = Request.objects.all()
    return render(request, 'requests.html', {'reqs': reqs})