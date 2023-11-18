
from rest_framework import serializers
from .models import Product, Brand, ProductImages 

class ProductImagesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProductImages
        fields = ['image']


        

class ProductListSerializer(serializers.ModelSerializer):
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



class ProductDetailSerializer(serializers.ModelSerializer):

    brand = serializers.StringRelatedField()
    images = ProductImagesSerializer(source ='product_image', many= True)
    
    
    class Meta:
        model = Product
        fields = '__all__'







class BrandListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'





class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source ='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'


