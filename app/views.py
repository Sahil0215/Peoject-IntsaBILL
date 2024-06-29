from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def view_home_page(request):
    return render(request, 'home.html')


def login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username= username).exists():
            messages.error(request, 'Invaild Username')
            return redirect('/login/')
        user=authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invaild Password')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/dashboard/')



    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/')

def register_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        code=request.POST.get('code')


        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username Already Exist')
            return redirect('/register/')
        
        if code !="1974":
            messages.info(request, 'Enter Valid Code')
            return redirect('/register/')


        user=User.objects.create(
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, 'Account Created Successfully')
        return redirect('/register/')
    return render(request, 'register.html')


def success_page(request):
    return render(request, 'success.html')


@login_required(login_url="/login/")
def dashboard_page(request):
    return render(request, 'dashboard.html')
