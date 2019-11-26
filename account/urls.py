from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('edit_profile/<int:seller_id>', views.edit_profile, name="edit_profile"),
    path('edit_password/', views.edit_password, name="edit_password"),
    path('add_product/<int:seller_id>', views.add_product, name="add_product"),
]