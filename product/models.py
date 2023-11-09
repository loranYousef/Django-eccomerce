from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.aggregates import  Avg


# Create your models here.

PRODUCT_FLAG =(
    ('Sale','Sales'),
    ('Feature','Feature'),
    ('New','New'),

)
class Product(models.Model):

    name = models.CharField(_('name'),max_length=150)
    image = models.ImageField(_('image'),upload_to='products/', default='default.png')
    flag = models.CharField(_('flag'),max_length=10,choices=PRODUCT_FLAG)
    price = models.FloatField(_('price'))
    sku = models.IntegerField(_('sku'))
    brand = models.ForeignKey('Brand',verbose_name=('brand'),related_name='product_brand',on_delete=models.CASCADE)
    tags = TaggableManager()
    subtitle = models.TextField(_('subtitle'),max_length=500)
    description = models.TextField(_('description'),max_length=2800)
    quantity = models.IntegerField()
    slug= models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    
    def get_avg_rate(self):
        avg= self.product_review.aggregate(rate_avg=Avg('rate'))
        return avg

    
    
    






class ProductImages(models.Model):
    product =models.ForeignKey(Product,verbose_name=_('product'),related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    
    
    def __str__(self):
        return str(self.product)
    

 


class Brand(models.Model):
    name = models.CharField(_('brand'),max_length=50)
    image = models.ImageField(_('image'),upload_to='brand/')
    slug = models.SlugField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    


class Reviews(models.Model):
    user=models.ForeignKey(User, verbose_name=_('user'),related_name='review_author', on_delete=models.SET_NULL,null=True,blank=True)
    product =models.ForeignKey(Product,verbose_name=_('product'),related_name='product_review',on_delete=models.CASCADE)
    comment= models.CharField(_('comment'),max_length=200)
    rate = models.IntegerField(_('rate'))
    created_at= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.product)
    


