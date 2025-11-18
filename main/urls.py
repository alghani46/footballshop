from django.urls import path,include
from . import views
from .views import create_product_flutter,my_products_flutter
app_name = "main" 
urlpatterns = [
    path('', views.home, name='home'),
    path("add/", views.add_product, name="add_product"),
    path("product/<int:id>/", views.product_detail, name="product_detail"),
    path("xml/", views.show_xml, name="show_xml"),
    path("json/", views.show_json, name="show_json"),
    path("xml/<int:id>/", views.show_xml_by_id, name="show_xml_by_id"),
    path("json/<int:id>/", views.show_json_by_id, name="show_json_by_id"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("product/<int:id>/edit/", views.edit_product, name="edit_product"),
    path("product/<int:id>/delete/", views.delete_product, name="delete_product"),
    path('api/products/', views.products_json, name='products_json'),
    path('api/products/<int:id>/', views.product_json_by_id, name='product_json_by_id'),
    path('api/products/create/', views.add_product_ajax, name='add_product_ajax'),
    path('api/products/<int:id>/update/', views.update_product_ajax, name='update_product_ajax'),
    path('api/products/<int:id>/delete/', views.delete_product_ajax, name='delete_product_ajax'),
    path('api/auth/login/', views.login_ajax, name='login_ajax'),
    path('api/auth/register/', views.register_ajax, name='register_ajax'),
    path('api/auth/logout/', views.logout_ajax, name='logout_ajax'),
    path("auth/", include("authentication.urls")),
    path("create-flutter/", create_product_flutter, name="create_product_flutter"),
    path("api/flutter/my-products/", my_products_flutter, name="my_products_flutter"),
]
