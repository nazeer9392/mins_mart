from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout



def register(request):
    if request.method =='POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username=request.POST['username']
        email =request.POST['email']
       
        password =request.POST['password']
        
        user=User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email)
        user.set_password(password)
        user.save()
        return redirect('login')
    
    return render(request, 'register.html')

def logout_(request):
    logout(request)
    return render(request, 'logout.html')


# Create your views here.
