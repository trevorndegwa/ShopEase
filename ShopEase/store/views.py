from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Define the 'home' view to display products on the homepage
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

# Define the 'about' view to render the about page
def about(request):
    return render(request, 'about.html', {})

# Define the 'login_user' view to render the login page
def login_user(request):
    return render(request, 'login.html', {})

# Define the 'logout_user' view to render the logout page
def logout_user(request):
    pass
