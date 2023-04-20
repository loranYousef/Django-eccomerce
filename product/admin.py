from django.contrib import admin


# Register your models here.
from .models import Product , ProductImages , Brand , Reviews

class ProductImagesAdmin(admin.TabularInline):
    model= ProductImages 

class ProductAdmin(admin.ModelAdmin):
    
    list_display=['name','brand','price']
    list_filter=['brand','price']
    inlines= [ProductImagesAdmin]
    search_fields= ['name','subtitle','description']
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','rate','comment','created_at']
    list_filter=['rate','created_at']
    search_fields=['user','product','comment']
    





admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Reviews,ReviewAdmin)
admin.site.site_header = "Project Admin"