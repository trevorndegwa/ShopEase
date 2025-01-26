from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    names = models.CharField(max_length=250)
    email = models.EmailField(max_length=250) 
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, default="United States")
    county = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250)
    postalcode = models.CharField(max_length=250, null=True, blank=True)

    # Admin backend don't pluralise "Shipping Address"
    class Meta:
        verbose_name_plural = "Shipping Address"
        ordering = ['names']  # Order by names

    def __str__(self):
        return f'{self.names} - {self.address1}, {self.city}'

# Create a user shipping address
def create_shipping(sender, instance, created, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()
post_save.connect(create_shipping, sender=User)

# Create Order model
class Order(models.Model):
    # Foreign Key to User model (on_delete handles what happens when a user is deleted)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Basic order information
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)

    # Shipping details (consider splitting this into more structured fields if necessary)
    shipping_address = models.TextField(max_length=14000)

    # Amount paid (ensure you handle currency appropriately)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)

    # Dates related to the order (auto_now_add will add the date when the order is created)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        # Use f-string formatting for cleaner string representation
        return f'Order {self.id} - {self.full_name}'

# Create model for Order Items
class OrderItem(models.Model):
    # Foreign Keys for relationships to Order, Product, and User models
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Quantity and price information for each order item
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        # Return a more descriptive string representation using product name and order ID
        return f'Order Item {self.id} - {self.product.name} (x{self.quantity})'
