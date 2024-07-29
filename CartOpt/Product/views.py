from django.shortcuts import render
from django.views import View
from .models import Product
from django.contrib.auth.models import User
from Cart.models import TheCart

class ProdView(View):
    def get(self, request):
        products = Product.objects.all().order_by('title')
        return render(request, "Product/index.html", {
            'products': products
        })
