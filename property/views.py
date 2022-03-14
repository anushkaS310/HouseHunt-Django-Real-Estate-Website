from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .form import PropertyForm
from .models import Property
# Create your views here.
@login_required(login_url='login')
def upload(request):
    if request.method=='POST':
        form =PropertyForm(request.POST)
        if form.is_valid():
            property= Property(
                user_id=request.user.id,
                # user_name=request.user.first_name,
                title=form.cleaned_data['title'],
                type=form.cleaned_data['type'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zipcode=form.cleaned_data['zipcode'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                bathroom=form.cleaned_data['bathroom'],
                availibility=form.cleaned_data['availibility'],
                garage=form.cleaned_data['garage'],
                gym=form.cleaned_data['gym'],
                swimming_pool=form.cleaned_data['swimming_pool'],
                furnishing=form.cleaned_data['furnishing'],
                sqft=form.cleaned_data['sqft'],
                lot_size=form.cleaned_data['lot_size']
            )
            property.save()
            return redirect('dashboard')
    else:
        form =PropertyForm()
    return render(request,'properties/upload_form.html',{
        "form":form,
    })
    
from django.shortcuts import render

# Create your views here.
