from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem

# On the admin site, register the models
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)
