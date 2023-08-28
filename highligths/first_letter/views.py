from django.shortcuts import render
from  .models import Product

def first(request):
    products= Product.objects.filter(name__startswith=letter)
    return render(request, 'first.html', {'products': products})