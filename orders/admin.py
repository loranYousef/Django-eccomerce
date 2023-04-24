from django.contrib import admin
from .models import Order , OrderDetail

admin.site.register(Order)
admin.site.register(OrderDetail)