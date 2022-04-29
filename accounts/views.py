from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from property.models import Property
from django.db.models import Q
from django.contrib import auth
from django.views.decorators.cache import cache_control
import re
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
        special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already taken!")
                return redirect('register')
            else:
                if special_char.search(first_name)!=None or special_char.search(last_name)!=None:
                    messages.error(request,"Name must only contain alphabets!")
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

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'accounts/dashboard.html')
    else:
        return redirect('homepage')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def db_upload(request):
    if request.user.is_authenticated:
        context={}
        context["properties"]=Property.objects.filter(Q(published=True) & Q(uid=request.user.id,))
        bookmarks=request.session.get("bookmarks")
        if bookmarks is None or len(bookmarks) == 0 :
            context["property"] = []
            context["check"] = False
        else:
            property=Property.objects.filter(id__in=bookmarks)
            context["property"] = property
            context["check"] = True
        return render(request,'accounts/db_upload.html',context)
    else:
        return redirect('homepage')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def db_bookmark(request):
    if request.user.is_authenticated:
        context={}
        bookmarks=request.session.get("bookmarks")
        if bookmarks is None or len(bookmarks) == 0 :
            context["property"] = []
            context["check"] = False
        else:
            property=Property.objects.filter(Q(published=True)&Q(id__in=bookmarks))
            context["property"] = property
            context["check"] = True
        return render(request,'accounts/db_bookmark.html',context)
    else:
        return redirect('homepage')

    

def logout(request):
    auth.logout(request)
    return redirect ('homepage')
    # print("sara")
    # if request.method == "POST":
    #     auth.logout(request)
    #     print("sara")
    #     messages.success(request, 'Logout Successful!')
    #     return redirect('homepage')