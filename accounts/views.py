from django.shortcuts import render, redirect
from .models import Customer

def register(request):
    if request.method == 'POST':
        Customer.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address']
        )
        return redirect('login')
    return render(request, 'user/register.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = Customer.objects.filter(email=email).first()
        if user:
            request.session['user_id'] = user.id
            return redirect('user_home')
    return render(request, 'user/login.html')


def logout_user(request):
    request.session.flush()
    return redirect('login')
