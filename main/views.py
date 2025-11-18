
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.http import JsonResponse
import json




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
    # Page renderer only; AJAX posts must go to /api/auth/register (register_ajax)
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})
    return HttpResponse(status=405)  # Method Not Allowed (use AJAX endpoint)


def login_user(request):
    # Page renderer only; AJAX posts must go to /api/auth/login (login_ajax)
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    return HttpResponse(status=405)  # Method Not Allowed (use AJAX endpoint)


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

@csrf_exempt
def create_product_flutter(request):
    if request.method != 'POST':
        return JsonResponse(
            {"status": "error", "message": "Invalid method"},
            status=405,
        )

    # Must be logged in , CookieRequest will send the session cookie
    if not request.user.is_authenticated:
        return JsonResponse(
            {"status": "error", "message": "Not authenticated"},
            status=401,
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"status": "error", "message": "Invalid JSON"},
            status=400,
        )

    name = strip_tags(data.get("name", "").strip())
    description = strip_tags(data.get("description", "").strip())
    category = data.get("category", "")
    thumbnail = data.get("thumbnail", "")
    is_featured = data.get("is_featured", False)
    price_raw = data.get("price", 0)

    try:
        # adjust as needed
        price = int(price_raw)
    except (TypeError, ValueError):
        return JsonResponse(
            {"status": "error", "message": "Invalid price"},
            status=400,
        )

    new_product = Product(
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        price=price,
        user=request.user,   # ALWAYS the logged-in user
    )
    new_product.save()

    return JsonResponse(
        {"status": "success", "id": new_product.id},
        status=200,
    )


def my_products_flutter(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {"detail": "Authentication credentials were not provided."},
            status=401,
        )

    qs = Product.objects.filter(user=request.user).order_by('-id')
    data = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "thumbnail": p.thumbnail,
            "category": p.category,
            "is_featured": p.is_featured,
        }
        for p in qs
    ]
    return JsonResponse(data, safe=False)


@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
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



@login_required(login_url='/login/')
def products_json(request):
    qs = Product.objects.filter(user=request.user).order_by('-id')
    data = [{
        "id": p.id, "name": p.name, "description": p.description, "price": p.price,
        "category": p.category, "thumbnail": p.thumbnail, "is_featured": p.is_featured,
    } for p in qs]
    return JsonResponse(data, safe=False)

@login_required(login_url='/login/')
def product_json_by_id(request, id):
    p = Product.objects.filter(user=request.user, pk=id).first()
    if not p:
        return JsonResponse({'detail':'Not found'}, status=404)
    data = {
        "id": p.id, "name": p.name, "description": p.description, "price": p.price,
        "category": p.category, "thumbnail": p.thumbnail, "is_featured": p.is_featured,
    }
    return JsonResponse(data)

@csrf_exempt
@require_POST
@login_required(login_url='/login/')
def add_product_ajax(request):
    Product.objects.create(
        user=request.user,
        name=request.POST.get('name', '').strip(),
        description=request.POST.get('description', ''),
        price=request.POST.get('price') or 0,
        category=request.POST.get('category', ''),
        thumbnail=request.POST.get('thumbnail', ''),
        is_featured=request.POST.get('is_featured') == 'on',
    )
    return HttpResponse(b'CREATED', status=201)

@csrf_exempt
@require_POST
@login_required(login_url='/login/')
def update_product_ajax(request, id):
    p = Product.objects.filter(user=request.user, pk=id).first()
    if not p: return HttpResponse(status=404)
    p.name = request.POST.get('name', p.name)
    p.description = request.POST.get('description', p.description)
    p.price = request.POST.get('price') or p.price
    p.category = request.POST.get('category', p.category)
    p.thumbnail = request.POST.get('thumbnail', p.thumbnail)
    p.is_featured = (request.POST.get('is_featured') == 'on')
    p.save()
    return HttpResponse(b'UPDATED', status=200)

@csrf_exempt
@require_POST
@login_required(login_url='/login/')
def delete_product_ajax(request, id):
    p = Product.objects.filter(user=request.user, pk=id).first()
    if not p: return HttpResponse(status=404)
    p.delete()
    return HttpResponse(b'DELETED', status=200)


@require_POST
def login_ajax(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse({'ok': False, 'error': 'Invalid credentials'}, status=400)

    prev = user.last_login
    login(request, user)
    resp = JsonResponse({'ok': True, 'username': user.username})
    resp.set_cookie('last_login', prev.strftime("%Y-%m-%d %H:%M") if prev else 'First login!')
    return resp

@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if not form.is_valid():
        # Return Django form errors as JSON
        return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
    form.save()
    return JsonResponse({'ok': True})

@require_POST
def logout_ajax(request):
    logout(request)
    resp = JsonResponse({'ok': True})
    resp.delete_cookie('last_login')
    return resp




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


