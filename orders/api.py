from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Order, OrderDetail, Cart, CartDetail
from .serializers import CartSerializer
from django.contrib.auth.models import User


class CartDetailCreateApi(generics.GenericAPIView):


    def get(self,request,*args, **kwargs):
        user_name = self.kwargs['username']
        user = User.objects.get(username=user_name)
        cart =Cart.objects.get(user=user, cart_status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})





