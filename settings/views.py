from django.shortcuts import render
from product.models import Product, Brand, Reviews
from django.db.models import Count

# Create your views here.

def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))
    item_sale= Product.objects.filter(flag='Sale')[:10]
    
    
    
    
    
    return render(request,'settings/home.html',{
        'brands':brands,
        'item_sale':item_sale,
    })
