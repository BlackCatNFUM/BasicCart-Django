from django.urls import path
from .views import *

app_name='Product'
urlpatterns = [
    path('', ProdView.as_view(), name='view')
]