from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django import forms


# Define the 'product' view to display details of a specific product
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def category_summary(request):
    return render(request, 'category_summary.html', {})

def category(request, filler):
    # Hyphens substituted with empty spaces
    filler = filler.replace('-', ' ')
    # Obtain the category from the url
    try:
       # Search the category
       category = Category.objects.get(name=filler)
       products = Product.objects.filter(category=category)
       return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("That category doesn't exist"))
        return redirect('home')

# Define the 'home' view to display products on the homepage
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

# Define the 'about' view to render the about page
def about(request):
    return render(request, 'about.html', {})

# Define the 'register_user' view to handle user registration and render the registration page
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log in the user
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, ("You've registered successfully! Karibu!"))
            return redirect('home')
        else:
            messages.success(request, ("Oops! There's an issue with your registration, please try again.."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})

# Define the 'login_user' view to handle user login and render the login page
def login_user(request):
    # Check if the request method is POST (indicating form submission)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # If authentication is successful, log the user in
        if user is not None:
            login(request, user)
            messages.success(request, ("You've been logged in"))
            return redirect('home')
        else:
            # If authentication fails, display an error message
            messages.success(request, ("There's a problem, please try again")) 
            return redirect('login')
    else:
        return render(request, 'login.html', {}) 

# Define the 'logout_user' view to handle user logout
def logout_user(request):
    logout(request)
    messages.success(request, ("You've been logged out"))
    return redirect('home')
