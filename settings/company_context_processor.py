from .models import Company

def get_data(request):
    data = Company.objects.first()
    return {'site_data':data}