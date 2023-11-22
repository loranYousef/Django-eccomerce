from django.urls import path
from .views import OrderList
from .api import CartDetailCreateApi, OrderListApi

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),



    # api
    path('api/<str:username>/cart', CartDetailCreateApi.as_view()),
    path('api/<str:username>/orders', OrderListApi.as_view()),
]
