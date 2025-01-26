from django.shortcuts import render

def payment_successful(request):
    return render(request, "payment/payment_successful.html", {})
