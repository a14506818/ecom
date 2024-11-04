from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def home(request):
    products = Product.objects.all()
    all_cate = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'all_cate': all_cate})

def about(request):
    return render(request, 'about.html', {})

def run_login(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        messages.success(request, ("Successfully Login !"))
        return redirect('home')
    else:
        messages.error(request, ("Login Error !"))
        return redirect('login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        return run_login(request, username, password)
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully Logout !"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            return run_login(request, username, password)
        else:
            messages.error(request, ("Register Error !"))
            return redirect('register')
    return render(request, 'register.html', {'form': form})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def category(request, pk):
    all_cate = Category.objects.all()
    try:
        category = Category.objects.get(id=pk)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products,
                                                  'category':category, 'all_cate': all_cate})
    except:
        messages.error(request, ("Category not found !"))
        return redirect('home')
