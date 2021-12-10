from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid detials")
            return redirect('register')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=name).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                 user=User.objects.create_user(username=name,password=password1,email=email)
                 user.save();
                 print("user created")
        else:
            print("password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
