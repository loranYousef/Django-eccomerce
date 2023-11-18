
from rest_framework import serializers
from .models import Product, Brand



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField()   #--add a column by adding function def get_ lecture 43
    # price_with_tax = serializers.SerializerMethodField(method_name='myfunc') --add a column by adding function
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_price_with_tax(self,product):
        return product.price*1.1
    
    # def myfunc(self,product):
    #     return product.price*1.1