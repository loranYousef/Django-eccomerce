from typing import Any
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.db.models import Count
from .models import Product , Brand
from django.db.models import Q, F

# Q when we use (and, or) for serach lookup
# F when say the value of column = value of another column (price(value) = quantity(value))


def query_Debug(request):
    # data = Product.objects.filter(name__contains='Noah',price__gt=70)
    # data = Product.objects.filter(Q(name__contains='Noah') & Q(price__gt=20))
    # data = Product.objects.filter(price = F('quantity')) F mean Reference 
    # data = Product.objects.filter(price__gt=70).order_by('name').reverse()
    # data = Product.objects.order_by('name')
    # data = Product.objects.earliest('name')
    # data = Product.objects.latest('name')
    # data = Product.objects.values('name','id','price') --- fields that we want to appear in template 
    # data = Product.objects.values_list('name','id','brand__name')
    # data = Product.objects.prefetch_related('brand').all() used with many ot many 
    # data = Product.objects.select_related('brand').all() used with one to one and freignkey
    data = Product.objects.select_related('brand').all()
    

    return render(request,'product/productlist.html',{'data': data})





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
    