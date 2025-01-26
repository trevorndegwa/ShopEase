from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Category, Customer, Product, Order

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile

# Customise the User admin to integrate Profile
class CustomUserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]

# Unregister the default User admin and register the customised version
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
