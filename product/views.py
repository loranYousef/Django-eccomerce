from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.db.models import Count
from .models import Product , Brand




class ProductList(ListView):
    model = Product 
    paginate_by = 1


class ProductDetail(DetailView):
    model = Product 


class BrandList(ListView):
    model = Brand
    paginate_by = 1
    queryset = Brand.objects.all().annotate(product_count= Count('product_brand'))


class Brand_Detail(DetailView):
    model = Brand
    # queryset = Brand.objects.filter(slug=slug).annotate(product_count= Count('product_brand'))
    def get_queryset(self):
        queryset = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count= Count('product_brand'))
        return queryset
    