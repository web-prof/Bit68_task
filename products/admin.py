from django.contrib import admin
from .models import Products


class Products_admin(admin.ModelAdmin):
    model = Products
    list_display = ['prd_name','prd_owner','prd_seller','prd_price']


admin.site.register(Products, Products_admin)
