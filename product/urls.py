from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('product_list/', views.product_list, name="product_list"),
    path('product_page/<int:book_id>', views.product_page, name="product_page"),
]