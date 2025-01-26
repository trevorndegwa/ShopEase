from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, PasswordChangeForm, UserInfoForm
from django import forms
from django.contrib.auth.decorators import login_required


# Define the 'product' view to display details of a specific product
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

# Defines the view for products  in the cart
def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})

# Showcases the 'category' view to house product types 
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
            messages.success(request, ("Please fill out your user information below"))
            return redirect('update_info')
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

# Defines 'update_user' to take in profile updates from user
@login_required
def update_user(request):
    # Retrieve the current user instance
    current_user = get_object_or_404(User, id=request.user.id)

    # Populate the form with POST data or existing user data
    user_form = UserUpdateForm(data=request.POST or None, instance=current_user)

    # Process form submission
    if request.method == "POST" and user_form.is_valid():
        user_form.save()
        login(request, current_user)  # Re-authenticate user
        messages.success(request, "Your profile has been updated successfully!")
        return redirect('home')

    # Render the profile update page with the form
    return render(request, "update_user.html", {"user_form": user_form})

# Defines 'update_password' to take in password changes
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        
        if request.method == "POST":
            form = PasswordChangeForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Password updated")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = PasswordChangeForm(current_user)   
 
        return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "You must be logged in to view page!")

# Defines 'update_info' for extending user profile on app
@login_required
def update_info(request):

    # Retrieve the current user instance
    current_user = get_object_or_404(Profile, user__id=request.user.id)

    # Populate the form with POST data or existing user data
    user_form = UserInfoForm(data=request.POST or None, instance=current_user)

    # Process form submission
    if request.method == "POST" and user_form.is_valid():
        user_form.save()
        messages.success(request, "Your info has been updated successfully!")
        return redirect('home')

    # Render the profile update page with the form
    return render(request, "update_info.html", {"user_form": user_form})

def search(request):
    return render(request, "search.html", {})
