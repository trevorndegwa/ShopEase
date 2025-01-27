from django.contrib import admin
from django.contrib.auth.models import User
from .models import ShippingAddress, Order, OrderItem

# On the admin site, register the models
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)

# Creating OrderItem Inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

# Extend the Order Model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    fields = ["user", "full_name", "email", "shipping_address", "amount_paid", "date_ordered", "shipped", "date_shipped"]

    inlines = [OrderItemInline]

# Unregister the Order Model
admin.site.unregister(Order)
# Re-Register the Order && OrderAdmin
admin.site.register(Order, OrderAdmin)
