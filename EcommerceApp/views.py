from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here. 

def category(request, foo):
    foo = foo.replace('-',' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category= category)
        return render(request,"Category.html",{'products':products,'category':category})
    except:
        messages.success(request,("That Category Does Not Exist"))
        # return redirect('home')



def Product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {'product': product})

def Home(request):
    products = Product.objects.all()
    return render(request,"Home.html",{'products': products})

def Contact(request):
    return render(request,"ContactUS.html")

def About(request):
    return render(request,"about.html")

def Portfolio(request):
    return render(request,"Portfolio.html")

def login_user(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You Have Been Logged In"))
            return redirect('home')
        else:
            messages.success(request,("There was an error"))
            return redirect('login')

    else:
        return render(request,"login.html",{})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out... Thanks for shopping by")
    return redirect('home')

def register_user(request):
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user =  authenticate(username=username, password= password)
            login(request, user)
            messages.success(request,("You Have Registered Successfully "))
            return redirect('home')
        else:
            messages.success(request,("Whoos! There was an Problem... Please try again "))
            return redirect('register')
    else:    
        return render(request,"register.html",{"forms":form})


