from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    context = {
        'app_name': 'Football Shop',
        'student_name': 'Muhammad Rifqi Al Ghani',
        'student_class': 'KKI',
        'products': products,
    }
    return render(request, "main.html", context)
