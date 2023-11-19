from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


def order (request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.user = request.user
            request_obj.save()
            return redirect('order')
    else:
        form = RequestForm()

    return render(request, 'order.html', {'form': form, 'categories': DesignCategory.objects.all()})

def myorders(request):
    requests = Request.objects.filter(user=request.user)

    category_filter = request.GET.get('category')
    if category_filter:
        requests = requests.filter(category__name=category_filter)

    page = request.GET.get('page', 1)
    paginator = Paginator(requests, 5)
    try:
        requests = paginator.page(page)
    except PageNotAnInteger:
        requests = paginator.page(1)
    except EmptyPage:
        requests = paginator.page(paginator.num_pages)

    return render(request, 'myorders.html', {'requests': requests, 'categories': DesignCategory.objects.all(), 'category_filter': category_filter})

def delete_request(request, request_id):
    request_obj = get_object_or_404(Request, id=request_id)
    request_obj.delete()
    return redirect('myorders')

@login_required
def answers(request):
    user = request.user
    processed_orders = ClientOrder.objects.filter(client__user=user)

    page = request.GET.get('page', 1)
    paginator = Paginator(processed_orders, 5)

    try:
        processed_orders = paginator.page(page)
    except PageNotAnInteger:
        processed_orders = paginator.page(1)
    except EmptyPage:
        processed_orders = paginator.page(paginator.num_pages)

    return render(request, 'answers.html', {'processed_orders': processed_orders})


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
    category_filter = request.GET.get('category')
    if category_filter:
        reqs = reqs.filter(category__name=category_filter)

    page = request.GET.get('page', 1)
    paginator = Paginator(reqs, 5)
    try:
        reqs = paginator.page(page)
    except PageNotAnInteger:
        reqs = paginator.page(1)
    except EmptyPage:
        reqs = paginator.page(paginator.num_pages)

    return render(request, 'requests.html', {'requests': reqs, 'categories': DesignCategory.objects.all(), 'category_filter': category_filter})

def edit_order(request, order_id):
    request_obj = get_object_or_404(Request, id=order_id)

    try:
        order = ClientOrder.objects.get(client=request_obj)
    except ClientOrder.DoesNotExist:
        order = ClientOrder(client=request_obj)

    if request.method == 'POST':
        form = OrderAssignmentForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заказ успешно обработан.')
            return redirect('requests')  # Замените 'requests' на URL вашего представления со списком заказов
    else:
        form = OrderAssignmentForm(instance=order)

    return render(request, 'edit_order.html', {'form': form, 'order': request_obj})