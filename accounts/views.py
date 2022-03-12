from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,"Inavlid details!")
            return redirect('login')
    else:
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