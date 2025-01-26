from django.urls import path
from . import views

urlpatterns = [
    path('payment_successful', views.payment_successful, name='payment_successful'),
    path('checkout', views.checkout, name='checkout'),
]
