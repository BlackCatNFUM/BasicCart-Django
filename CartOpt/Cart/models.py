from django.db import models
from django.contrib.auth.models import User
from Product.models import Product
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


# Every User Should Have a Cart that has items in it
class TheCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    total_price = models.PositiveBigIntegerField(default=0)

    # Call The Function After Items Deleted or Added
    def update_total_price(self):
        self.total_price = sum(item.price for item in self.items.all())
        self.save()

    def __str__(self):
        return f"{self.user} : {self.total_price}$"


# The Items of the Cart
class CartItem(models.Model):
    cart = models.ForeignKey(TheCart, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.PositiveBigIntegerField(default=0)
    count = models.PositiveIntegerField(default=1)

    # Will return The Total Price of a Item that User Buy
    @property
    def total_price(self):
        return self.price * self.count

    def save(self, *args, **kwargs):
        self.price = int(self.item.price * self.count)
        super().save(*args, **kwargs)
        self.cart.update_total_price()

    # Delete the Item and Call the update_total_price function for applying the new price
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.cart.update_total_price()
    
    def __str__(self):
        return f"{self.item} from {self.cart}"
    

# calls update_total_price function after every save(new item added)
@receiver(post_save, sender=CartItem)
def update_cart_on_save(sender, instance, **kwargs):
    instance.cart.update_total_price()

# calls update_total_price function after every delete(item removed)
@receiver(post_delete, sender=CartItem)
def update_cart_on_delete(sender, instance, **kwargs):
    instance.cart.update_total_price()
