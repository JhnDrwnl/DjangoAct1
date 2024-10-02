from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='MenAvenue'),
    path('products', views.products, name='products'),
    path('cart', views.cart, name='cart')
]
