from django.shortcuts import render
from . models import Cars
from django.contrib.auth.models import User
from django.contrib import messages, auth 
from django.shortcuts import redirect



# Create your views here.

def home(request):
    car = Cars.objects.all()
    latest = Cars.objects.order_by('-id')[:3]
    return render(request,"home.html",{'car':car, 'latest': latest})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invailed crendentials")
            return redirect('/')

    return render(request, "login.html")





def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                
                return redirect('/')
        else:
            messages.error(request, "Password not matching !!")
            return redirect('register')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
