from rest_framework import serializers
from .models import Order, OrderDetail, Cart, CartDetail



class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = ['id','product','price','quantity','total']


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many = True)
    class Meta:
        model = Cart
        fields = '__all__'
        