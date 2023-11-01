from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.db.models import Count
from .models import Product , Brand




class ProductList(ListView):
    model = Product 


class ProductDetail(DetailView):
    model = Product 


class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.all().annotate(product_count= Count('product_brand'))


class Brand_Detail(DetailView):
    model = Brand