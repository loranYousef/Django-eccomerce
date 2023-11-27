from django.urls import path
from .views import signup, profile, edit_profile

app_name = 'accounts'

urlpatterns = [
    
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
]
