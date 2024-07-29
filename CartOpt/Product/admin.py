from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product

admin.site.register(Product, ProductAdmin)
