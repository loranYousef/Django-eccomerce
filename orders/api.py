from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Order, OrderDetail, Cart, CartDetail
from product.models import Product
from .serializers import CartSerializer, CartDetailSerializer, OrderSerializer
from django.contrib.auth.models import User


class OrderListApi(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request,*args, **kwargs):
        user = User.objects.get(username= self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)



class CartDetailCreateApi(generics.GenericAPIView):

    serializer_class = CartDetailSerializer

    def get(self,request,*args, **kwargs):      # add or creat a cart for users
        user_name = self.kwargs['username']
        user = User.objects.get(username=user_name)
        cart, created =Cart.objects.get_or_create(user=user, cart_status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})
    

    def post(self,request,*args, **kwargs):   # add data or Products to Cart
        user_name = self.kwargs['username']
        user = User.objects.get(username=user_name)

        product = Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data['quantity'])
    


        cart = Cart.objects.get(user=user, cart_status='Inprogress') # lecture 46 min:33:38
        cart_data,created = CartDetail.objects.get_or_create(cart =cart, product=product)
        cart_data.price = product.price
        cart_data.quantity = quantity
        cart_data.total = round(quantity*product.price,2)
        cart_data.save()
        return Response({'Status':200})
    

    def delete(self,request,*args, **kwargs):
        user = User.objects.get(username= self.kwargs['username']) # compine to lines
        product = Product.objects.get(id=request.data['product_id'])
        cart = Cart.objects.get(user=user, cart_status='Inprogress')
        cart_data = CartDetail.objects.get(cart =cart, product=product)
        cart_data.delete()
        return Response({'Status':200 , 'message': 'deleted Successfully'})

