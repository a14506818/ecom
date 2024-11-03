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
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

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