from django.urls import path
from .views import *

var_name1='cart'
app_name = "Cart"

urlpatterns = [
    path(f'{var_name1}/view', ViewCart.as_view(),name='view'),
    path(f'{var_name1}/add/<int:id>', AddToCart.as_view(),name='add'),
    path(f'{var_name1}/remove/<int:id>', RemoveFromCart.as_view(),name='remove')
]