from django.urls import path
from core import views

app_name = 'core_app'

urlpatterns = [
    path('cart/',views.cart, name='cart'),
    path('shop/',views.shop,name='shop'),
    path('single/',views.single,name='single'),
    path('checkout/',views.checkout,name='checkout')
]
