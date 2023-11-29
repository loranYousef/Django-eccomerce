from django.urls import path
from .views import OrderList, add_to_cart, remove_from_cart, checkout, invoice
from .api import CartDetailCreateApi, OrderListApi, CreateOrder

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),

    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('remove_from_cart', remove_from_cart, name='remove_from_cart'),
    path('checkout', checkout, name='checkout'),
    # path('invoice', invoice, name='invoice'),



    # api
    path('api/<str:username>/cart', CartDetailCreateApi.as_view()),
    path('api/<str:username>/orders', OrderListApi.as_view()),
    path('api/<str:username>/create_order', CreateOrder.as_view()),
]
