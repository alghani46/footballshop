
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def home(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'app_name': 'Football Shop',
        'student_name': 'Muhammad Rifqi Al Ghani',
        'student_class': 'KKI',
        'student_npm': '2406365396',
        'username': request.user.username,
        'products': products,
        'last_login': request.user.last_login,
    }
    return render(request, "main.html", context)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('main:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Simpan last login sebelumnya (sebelum Django update)
            previous_login = user.last_login  

            login(request, user)  # Django update last_login sekarang

            response = redirect("main:home")
            if previous_login:
                response.set_cookie("last_login", previous_login.strftime("%Y-%m-%d %H:%M"))
            else:
                response.set_cookie("last_login", "First login!")
            return response
        else:
            messages.error(request, "Username atau password salah!")

    # kalau GET request (atau login gagal) tampilkan halaman login
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})



def logout_user(request):
    logout(request)
    response = redirect('main:login')
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login/')
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user   # assign ke user yang login
            product.save()
            return redirect("main:home")
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})


@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("main:home")  # kembali ke halaman utama
    else:
        form = ProductForm(instance=product)

    return render(request, "edit_product.html", {"form": form, "product": product})



@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == "POST":
        product.delete()
        return redirect("main:home")

    return render(request, "delete_product.html", {"product": product})



def show_xml(request):
    data = serializers.serialize("xml", Product.objects.all())
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    data = serializers.serialize("json", Product.objects.all())
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    data = serializers.serialize("xml", [product])
    return HttpResponse(data, content_type="application/xml")

def show_json_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    data = serializers.serialize("json", [product])
    return HttpResponse(data, content_type="application/json")


