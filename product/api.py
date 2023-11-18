from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Product, Brand
from .serializers import ProductListSerializer,ProductDetailSerializer, BrandListSerializer,BrandDetailSerializer
from .pagination import MyPagination




@api_view(['GET'])
def productlist_api(request):
    products= Product.objects.all()
    data = ProductListSerializer(products,many=True, context={"request":request}).data
    return Response({'data':data})





class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = MyPagination



class ProducDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field= 'slug'

class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
    lookup_field= 'slug'