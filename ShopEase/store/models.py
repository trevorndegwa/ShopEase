from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime
from django.dispatch import receiver

# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=110)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Customer profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=15, blank=True)
    address1 = models.CharField(max_length=250, blank=True)
    address2 = models.CharField(max_length=250, blank=True)
    county = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    postalcode = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    prev_cart = models.CharField(max_length=250, blank=True, null=True) # Convert cart to string (later back to dict)

    def __str__(self):
        return self.user.username

# Create a user's profile by default on registration
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Product categories
class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

# Entirety of our products
class Product(models.Model):
    name = models.CharField(max_length=110)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    # Add some sale effects
    is_on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name  

# Orders from customers
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=110, default='', blank=True)
    phone = models.CharField(max_length=25, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
