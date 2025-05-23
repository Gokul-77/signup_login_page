from django.shortcuts import render,redirect
from .models import signup,login
from django.utils import timezone

def signuppage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        time = timezone.now()
        
        if signup.objects.filter(email=email).exists():
            return redirect('loginpage')
        else:
            signup.objects.create(name=name, place=place, email=email, mobile=mobile, created_at=time)
            return redirect('success')
    return render(request, 'signup.html')

def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        time = timezone.now()
        if signup.objects.filter(email=email,mobile=mobile).exists():
            login.objects.create(email=email, mobile=mobile, created_at=time)
            return redirect('success')
        else:
            return redirect('signuppage')
    return render(request, 'login.html')

def success(request):
    return render(request,'success.html')
