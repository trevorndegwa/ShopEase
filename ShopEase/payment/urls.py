from django.urls import path
from . import views

urlpatterns = [
    path('payment_successful', views.payment_successful, name='payment_successful'),
    path('checkout', views.checkout, name='checkout'),
    path('billing_info', views.billing_info, name='billing_info'),
    path('order_process', views.order_process, name='order_process'),
    path('dash_shipped', views.dash_shipped, name='dash_shipped'),
    path('dash_not_shipped', views.dash_not_shipped, name='dash_not_shipped'),
]
