from django.shortcuts import render
from product.models import Product, Brand, Reviews
from django.db.models import Count

# Create your views here.

def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))
    item_sale= Product.objects.filter(flag='Sale')[:10]
    item_feature= Product.objects.filter(flag='Feature')[:6]
    item_new= Product.objects.filter(flag='New')[:12]
    reviews = Reviews.objects.all()[:6]
    
    
    
    
    
    return render(request,'settings/home.html',{
        'brands':brands,
        'item_sale':item_sale,
        'item_feature':item_feature,
        'item_new':item_new,
        'reviews':reviews,
        
    })
