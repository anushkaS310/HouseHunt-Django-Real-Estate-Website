from django.shortcuts import render
from .form import PropertyForm
# Create your views here.
def upload(request):
    form =PropertyForm(request.POST)
    return render(request,'properties/upload_form.html',{
        "form":form,
    })
    
