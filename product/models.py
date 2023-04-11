from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _

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

    def __str__(self):
        return self.name
    
     






class ProductImages(models.Model):
    pass
    '''
    product:foreignkey
    image

    '''



class Brand(models.Model):
    pass
    '''
    name
    image
    
    '''


class Reviews(models.Model):
    pass
    '''
    user
    product
    review
    date
    rate
    '''