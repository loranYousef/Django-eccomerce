from django.urls import path
app_name = 'product'

from .views import ProductList,ProductDetail,BrandList,Brand_Detail, query_Debug, add_review

urlpatterns = [
    path('debug', query_Debug , name='query_debug'),
    path('' , ProductList.as_view(), name='product_list'),
    path('<slug:slug>' , ProductDetail.as_view() , name='product_detail'),
    path('<slug:slug>/add_review' , add_review, name='add_review'),
    path('brands/',BrandList.as_view(), name ='brand_list'),
    path('brands/<slug:slug>',Brand_Detail.as_view(), name ='brand_detail'),

]
