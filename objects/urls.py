from django.urls import path 
from . import fetch_product
urlpatterns = [
    path('product/', fetch_product.fetch_shopify_data),
    # Add more URL patterns as needed
]
