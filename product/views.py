from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView , DetailView
from django.db.models import Count
from .models import Product , Brand, Reviews
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField , FloatField
from django.db.models.aggregates import Sum , Avg, Min , Max , Count
from django.db.models.functions import Concat
from .forms import ProductReviewForm
from django.http import JsonResponse
from django.template.loader import render_to_string

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
    # data = Product.objects.aggregate(min_price=Min('price'),avg_price=Avg('price'))
    # data = Product.objects.annotate(is_new=F('quantity')*2) add column for counting
    # data = Product.objects.annotate(full_name =Concat('name',Value(' '),'flag'))
    dis_price=ExpressionWrapper(F('price')*.8, output_field=DecimalField())
    data = Product.objects.annotate(discounted_price=dis_price)
    

    return render(request,'product/productlist.html',{'data': data})





class ProductList(ListView):
    model = Product 
    paginate_by = 50


class ProductDetail(DetailView):
    model = Product 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["reviews"] = Reviews.objects.filter(product=self.get_object())
        return context
    
    


def add_review(request,slug):
    product= Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            myform= form.save(commit=False)
            myform.user = request.user
            myform.product = product
            myform.save()

    reviews= Reviews.objects.filter(product=product)
    html = render_to_string('include/all_reviews.html',{'reviews':reviews, request:request})


    
    return JsonResponse({'result':html})


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


