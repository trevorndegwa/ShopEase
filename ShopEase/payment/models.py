from django.db import models
from django.contrib.auth.models import User

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

