from django.shortcuts import render,redirect
from . models import Product,Cart
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def home(request):
    prds=Product.objects.all()
    Cartproduct=Cart.objects.all()
    cartcount=Cartproduct.count()
    return render(request, 'home.html', {'product':prds,'count':cartcount})

def product_desc(request,p_id):
    prod=Product.objects.get(id=p_id)
    return render(request, 'product_desc.html',{'product':prod})

# def contact(request):
#     return render (request ,'contact.html')

def login_(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect('admin')
            
            return redirect('home')
            
        else:
            return render(request,'login.html',{'bool':True})
    return render(request, 'login.html')

def admin(request):
    return render(request, 'admin.html')

def profile(request):
    Cartproduct=Cart.objects.all()
    cartcount=Cartproduct.count()
    return render(request, 'profile.html',{'count':cartcount})

@login_required(login_url='login')
def cart(request):
    cartproducts=Cart.objects.all
    Cartproduct=Cart.objects.all()
    cartcount=Cartproduct.count()
    return render(request, 'cart.html',{'context':cartproducts ,'count':cartcount})

@login_required(login_url='login')
def addtocart(request,id):
    p=Product.objects.get(id=id)
    try:
        c=Cart.objects.get(name=p.name,host=request.user)
        c.quantity+=1
        c.totalprice+=p.price
        c.save()
        
    except:
        Cart.objects.create(name=p.name,price=p.price,image=p.image,desc=p.desc,totalprice=p.price,host=request.user)
    return redirect('cart')

def delete(request,id):
    a=Cart.objects.get(id=id)
    a.delete()
    return redirect('cart')

def checkout(request):
    return render(request, 'checkout.html')
    
    
from django.db.models import Q

def search_results(request):
    query = request.GET.get('search')
    results = []
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(desc__icontains=query)
        )
    return render(request,'search_results.html',{'results': results, 'query':query})



# Create your views here.