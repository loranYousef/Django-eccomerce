from django.contrib import admin

# Register your models here.
from .models import Product , ProductImages , Brand , Reviews


admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Reviews)
