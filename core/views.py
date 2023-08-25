from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'hompage/index.html')

def cart(request):
    return render(request,'hompage/cart.hmtl')

def shop(request):
    return render(request,'hompage/shop.html')

def single(request):
    return render(request,'hompage/single_product.html')

def checkout(request):
    return render(request,'hompage/checkout.html')