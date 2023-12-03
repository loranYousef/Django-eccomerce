from django.urls import path
from .views import signup, profile, edit_profile, dashboard, activate_account, test_send

app_name = 'accounts'

urlpatterns = [
    
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('<str:username>/activate', activate_account, name='activate_account'),
    path('dashboard', dashboard, name='dashboard'),


    path('test-celery', test_send, name='test_send'),

    
    
]
