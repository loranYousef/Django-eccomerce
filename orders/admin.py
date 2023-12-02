from django.contrib import admin
from .models import Order , OrderDetail, Cart , CartDetail, Coupon

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_code','order_status','order_date','delivery_date']
    list_filter = ['order_status','order_date']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order','product','price','quantity','total']
    list_filter = ['price','quantity']




admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)

admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Coupon)
