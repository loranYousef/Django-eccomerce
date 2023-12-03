from django.shortcuts import render, redirect
from .models import Profile, Address, ContactNumbers
from .forms import SignupForm, ActivateUser
from django.core.mail import send_mail
from django.contrib.auth.models import User
from product.models import Product, Brand, Reviews
from orders.models import Order

# Create your views here.

def signup(request):
    if request.method =='POST':
        form =SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form.save()
            profile=Profile.objects.get(user__username=username)

            send_mail(
                "Activate Your Account",
                f"Wellcome {username}\n use this code {profile.code} to activate your account ... \n Green_Store",
                "lpythondeveloper0@gmail.com",
                ["{{email}}"],
                fail_silently=False,
            )
        return redirect(f'/account/{username}/activate')

    else:
        form=SignupForm()

    return render(request,'accounts/signup.html',{'form':form})



def activate_account(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = ActivateUser(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''
                profile.save()
                return redirect('/accounts/login')

    else:

        form = ActivateUser()
    return render(request,'accounts/activate.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    address = Address.objects.filter(user=request.user)
    contact_numbers = ContactNumbers.objects.filter(user=request.user)
    return render(request,'accounts/profile.html',{ 'profile':profile, 'address':address, 'contact_numbers':contact_numbers})





def edit_profile(request):
    pass


def dashboard(request):
    users = User.objects.all().count()
    products = Product.objects.all().count()
    reviews = Reviews.objects.all().count()
    brands = Brand.objects.all().count()
    orders = Order.objects.all().count()


    recieved = Order.objects.filter(order_status='Recieved').count()
    processed = Order.objects.filter(order_status='Processed').count()
    shipped = Order.objects.filter(order_status='Shipped').count()
    delivered = Order.objects.filter(order_status='Delivered').count()

    return render(request,'accounts/dashboard.html',{
        'users': users,
        'products':products ,
        'reviews':reviews ,
        'brands':brands ,
        'orders':orders ,
        'recieved':recieved ,
        'processed':processed ,
        'shipped':shipped ,
        'delivered':delivered ,
    })

from.tasks import send_build_emails
def test_send(request):
    send_build_emails.delay(5)

    return render(request,'test_celery.html', {})