from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate ,logout , login
# Create your views here.

def index(request):
    dests = Destination.objects.all()
    return render(request , 'index.html',{'dests':dests})

def register(request):
    if request.method == 'POST':
        Firstname = request.POST['first_name']
        Lastname = request.POST['last_name']
        Username = request.POST['username']
        Password = request.POST['password']
    
        user = User.objects.create_user(first_name = Firstname , last_name = Lastname , username = Username , password = Password)
        user.save()

        return redirect('/')
    else:   
        return render(request , 'register.html')
    
    
def Login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        user = authenticate(username = Username , password = Password)
        if user is not None:
            login(request , user)
            return redirect('/' , {'Username':Username})
        else:
            
            return redirect('/login')
    else:   
        return render(request , 'login.html')

def Logout(request):
    logout(request)
    return redirect('/')
    