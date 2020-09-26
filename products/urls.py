
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('featured', views.products_featured, name='product_list'),
    path('<int:id>', views.product_detail, name='product_list'),
]