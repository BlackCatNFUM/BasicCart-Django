from django.contrib import admin
from .models import TheCart, CartItem


class CartItemAdmin(admin.StackedInline):
    model = CartItem

class TheCartAdmin(admin.ModelAdmin):
    model = TheCart
    inlines = [CartItemAdmin]

admin.site.register(TheCart, TheCartAdmin)