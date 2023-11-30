from django.db import models
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
from utils.generate_code import generate_code




CART_STATUS = (
    ('Inprogress', 'Inprogress'),
    ('Completed', 'Completed'),

)





class Cart(models.Model):
    
    user= models.ForeignKey(User,related_name='user_cart',on_delete=models.SET_NULL,null=True,blank=True)
    cart_status = models.CharField(max_length=10, choices= CART_STATUS, default='Inprogress')
    
    def cart_total(self):
        total = 0
        for product in self.cart_detail.all():
            if product.total is not None:    # this filed is from chatgpt its not a solving the issue but make the website work for now 
                total += product.total

        return round(total,2)
    
    
    

    # def __str__(self):
    #     return self.order_code
    



class CartDetail(models.Model):
    cart=models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product= models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL,null=True, blank=True)
    price =models.FloatField(null=True,blank=True)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.product)
    
    # def save(self, *args, **kwargs):
    #             # here if appear it again api well give error
    #    self.total =round(self.price * self.quantity,2)
    #    super(CartDetail, self).save(*args, **kwargs)
    #    print(self.total)
    









ORDER_STATUS = (
    ('Recieved', 'Recieved'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),

)





class Order(models.Model):
    order_code= models.CharField(max_length=10,default=generate_code)
    user= models.ForeignKey(User,related_name='user_order',on_delete=models.SET_NULL,null=True,blank=True)
    order_status = models.CharField(max_length=10, choices= ORDER_STATUS, default='Recieved')
    delivery_date = models.DateTimeField(null=True,blank=True)
    order_date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.order_code
    



class OrderDetail(models.Model):
    order=models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product= models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True, blank=True)
    price =models.FloatField()
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.order)
    
    def save(self, *args, **kwargs):
       self.total =self.price * self.quantity
       super(OrderDetail, self).save(*args, **kwargs) 
    



