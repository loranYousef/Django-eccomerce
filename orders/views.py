from django.shortcuts import render
from django.views.generic import ListView
from .models import Order


class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 1



def add_to_cart():
    pass



def remove_from_cart():
    pass


def checkout():
    pass

def invoice(request):
    pass 