from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname_shipping = models.CharField(max_length=250)
    email_shipping = models.EmailField(max_length=250)
    address1_shipping = models.CharField(max_length=250)
    address2_shipping = models.CharField(max_length=250, null=True, blank=True)
    country_shipping = models.CharField(max_length=250, default="Kenya")
    county_shipping = models.CharField(max_length=250, null=True, blank=True)
    city_shipping = models.CharField(max_length=250)
    postalcode_shipping = models.CharField(max_length=250, null=True, blank=True)

    # Admin backend don't pluralise "Shipping Address"
    class Meta:
        verbose_name_plural = "Shipping Address"
        ordering = ['fullname_shipping']  # Order by names

    def __str__(self):
        return f'{self.fullname_shipping} - {self.address1_shipping}, {self.city_shipping}'

