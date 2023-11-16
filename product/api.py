from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def productlist_api(request):
    products= Product.objects.all()
    data = ProductSerializer(products,many=True, context={"request":request}).data
    return Response({'data':data})





class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProducDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field= 'slug'