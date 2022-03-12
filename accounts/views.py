from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    if request== 'POST':
        return render(request,'accounts/login.html')
    return render(request,'accounts/login.html')


def register(request):
    if request.method =='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already taken!")
                return redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    messages.error(request,"email already in use!")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email= email,
                                                first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request,'Passwords do not match!')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')