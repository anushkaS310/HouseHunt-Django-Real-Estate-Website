from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from property.models import Property
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
# # Create your views here.
# @login_required(login_url='login')
# def contacts(request,property_id):
#     property=get_object_or_404(Property,pk=property_id)
#     return render(request,'contacts/contact.html',{
#         "property":property,
#     })
# @login_required(login_url='login')
def contact(request):
    if request.method=='POST':
        property_id=request.POST['property_id']
        property=request.POST['property_id']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        owner_email=request.POST['owner_email']
        if request.user.is_authenticated:
            user_id=request.user.id
            contacted=Contact.objects.all().filter(property_id=property_id,user_id=user_id)
            if contacted:
                messages.error(request,"you have already contacted")
                return redirect("/property/"+property_id)
        contact=Contact(property=property,property_id=property_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()
        send_mail(
            'Property Inquiry'
            'There is an inquiry for'+property+'by'+name+''
        )
    return redirect("/property/"+property_id)