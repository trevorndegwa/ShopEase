from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, PasswordChangeForm, UserInfoForm
from payment.models import ShippingAddress
from payment.forms import ShippingForm
from django import forms
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json

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
            
            # Get the current user 
            current_user = Profile.objects.get(user__id=request.user.id)
            # Retrieve saved cart from DB
            saved_cart = current_user.prev_cart
            # Convert string to python dictionary
            if saved_cart:
                # Using JSON, convert to dictionary
                json_cart = json.loads(saved_cart)
                # Added loaded dictionary to session
                cart = Cart(request)
                # Go through and add items in the cart
                for key,value in json_cart.items():
                    cart.add_db(product=key, quantity=value)

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
    if request.user.is_authenticated:
        # Get current user profile
        current_user = Profile.objects.get(user__id=request.user.id)
        # Get current user's shipping info
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        # Initialise user form with existing data or POST data
        user_form = UserInfoForm(request.POST or None, instance=current_user)
        # Initialize shipping form with existing data or POST data
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        # If either form is valid, save both forms
        if user_form.is_valid() or shipping_form.is_valid():
            user_form.save()  # Save the user info form
            shipping_form.save()  # Save the shipping info form
            messages.success(request, "Your Info Has Been Updated!!")
            return redirect('home')

        # Render the page with forms (including errors if forms are invalid)
        return render(request, "update_info.html", {'user_form': user_form, 'shipping_form': shipping_form})

    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('home')

def search(request):
    # Check if the user filled the form
    if request.method == "POST":
        asked = request.POST['asked']
        # Querying the DB model of Product
        asked = Product.objects.filter(Q(name__icontains=asked) | Q(description__icontains=asked))
        # Don't find when searching
        if not asked:
            messages.success(request, "That product is unavailable. Please try again") 
            return render(request, "search.html", {})
        else:
            return render(request, "search.html", {'asked':asked})
    else:
        return render(request, "search.html", {})
