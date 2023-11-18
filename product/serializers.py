
from rest_framework import serializers
from .models import Product, Brand, ProductImages , Reviews
from django.db.models.aggregates import Avg

class ProductImagesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProductImages
        fields = ['image']


        

class ProductListSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField()   #--add a column by adding function def get_ lecture 43
    # price_with_tax = serializers.SerializerMethodField(method_name='myfunc') --add a column by adding function
    avg_rate= serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_price_with_tax(self,product):
        return product.price*1.1
    
    def get_avg_rate(self,product):
        avg= product.product_review.aggregate(rate_avg=Avg('rate'))
        avg_rate = avg['rate_avg']
        if avg_rate:
            avg_rate = round(avg_rate,2)
        else:
            avg_rate = 0
        return  avg_rate

    def get_review_count(self,product):
        reviews = product.product_review.all().count()
        return reviews


    
    # def myfunc(self,product):
    #     return product.price*1.1


class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Reviews
        fields = ['comment','rate','created_at','user']










class ProductDetailSerializer(serializers.ModelSerializer):

    brand = serializers.StringRelatedField()
    images = ProductImagesSerializer(source ='product_image', many= True)
    avg_rate= serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    reviews = ProductReviewSerializer(source = 'product_review', many=True)
    
    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self,product):
        avg= product.product_review.aggregate(rate_avg=Avg('rate'))
        avg_rate = avg['rate_avg']
        if avg_rate:
            avg_rate = round(avg_rate,2)
        else:
            avg_rate = 0
        return  avg_rate

    def get_review_count(self,product):
        reviews = product.product_review.all().count()
        return reviews












class BrandListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'





class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source ='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'


