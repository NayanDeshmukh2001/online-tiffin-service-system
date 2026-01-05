from django.shortcuts import render
from .models import Tiffin

def user_home(request):
    tiffins = Tiffin.objects.filter(is_active=True)
    return render(request, 'user/home.html', {'tiffins': tiffins})
