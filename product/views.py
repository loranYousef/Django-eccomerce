from typing import Any
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.db.models import Count
from .models import Product , Brand




class ProductList(ListView):
    model = Product 
    paginate_by = 50


class ProductDetail(DetailView):
    model = Product 


class BrandList(ListView):
    model = Brand
    paginate_by = 50

    queryset = Brand.objects.all().annotate(product_count= Count('product_brand'))


class Brand_Detail(ListView):
    model = Product
    paginate_by = 50
    template_name = 'product/brand_detail.html'

    # queryset = Brand.objects.filter(slug=slug).annotate(product_count= Count('product_brand'))
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count= Count('product_brand'))

        data = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count= Count('product_brand'))[0]
        print(f"Brand : {data.name}")
        print(f"Brand : {data.image}")
        context["brand"] = data
        return context
    