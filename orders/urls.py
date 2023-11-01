from django.urls import path
from .views import OrderList


app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
]
