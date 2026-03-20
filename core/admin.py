from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Order

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_phone', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('client_name', 'client_phone', 'delivery_address')