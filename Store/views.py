from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def accueil(request):
    products=Product.objects.all()
    return render(request, 'store/index.html', context={"products":products})

def detail_product(request, slug):
    product=get_object_or_404(Product,slug=slug)
    return render(request, 'store/detail.html', {"product":product})

def add_to_cart(request):
    pass