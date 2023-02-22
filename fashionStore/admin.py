from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created_at', 'status', "shipping_name", "shipping_address", "payment_method", ]

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'brand', 'category', 'price', 'image', 'date', 'sale', 'percent']
    search_fields = ['name']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Category, CategoryAdmin)







