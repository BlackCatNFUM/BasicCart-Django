from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from Product.models import Product
from .models import TheCart, CartItem
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Return the Cart for view using request.user
class ViewCart(LoginRequiredMixin, View):
    login_url = "Account:login"
    def get(self, request):
        the_cart = get_object_or_404(TheCart, user=request.user)
        return render(request, "Cart/view_cart.html", {'cart': the_cart})

# Add Item To Cart
class AddToCart(LoginRequiredMixin, View):
    login_url = "Account:login"
    def post(self, request, id):
        
        # Get the Product By Id / Get the Count of that using request.POST.get
        prod = get_object_or_404(Product, id=id)
        prod_count = request.POST.get('count')

        # validating the Count
        if not prod_count:
            prod_count = 1
        else:
            prod_count = int(prod_count)
            if prod_count < 1:
                prod_count = 1


        try:    
            # Get the Cart
            cart, created = TheCart.objects.get_or_create(user=request.user)
            
            # Filter the CartItem using cart=cart and get the Item using item=prod
            cart_item, created = CartItem.objects.get_or_create(cart=cart, item=prod)
            # set the count of the item and save
            cart_item.count = prod_count
            cart_item.save()

            messages.success(request, f"{prod.title} Added To Cart")
            return redirect("/")
        
        except Exception as e:
            messages.error(request, f"Error : {e}")
            return redirect("/")


class RemoveFromCart(LoginRequiredMixin, View):
    login_url = "Account:login"
    def post(self, request, id):
        try:
            prod = get_object_or_404(Product, id=id)
            cart = get_object_or_404(TheCart, user=request.user)
            cart_item = get_object_or_404(CartItem, cart=cart, item_id=id).delete()
            messages.success(request, f"{prod.title} Removed From Your Cart Successfully")


            # if the user send req from index or viewcart
            # the user will automatically redirect to the page
            # that he/she was already in 
            referrer = request.META.get('HTTP_REFERER')
            if referrer:
                return redirect(referrer)
            else:
                return redirect('Cart:view')
        
        
        except Exception as e:
            messages.error(request, f"Error : {e}") 
            return redirect("/")
