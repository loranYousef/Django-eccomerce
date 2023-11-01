from django.shortcuts import render
from django.views.generic import ListView
from .models import Order


class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
