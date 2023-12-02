from .models import Cart, CartDetail



def get_or_create_cart(request):                   # show lecture 53  minute 37:27
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, cart_status ='Inprogress')
        if not created:
            cart_detail = CartDetail.objects.filter(cart=cart)
            return {'cart':cart, 'cart_detail':cart_detail}
        return {'cart':cart}
    else:
        return {}