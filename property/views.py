
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .form import PropertyForm
from .models import Property
from .dictionaries import type,fursnished,apartment_type,availibility,state_list
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
def property_list(request):
    properties=Property.objects.filter(published=True)
    print(properties[1].photo_main)
    paginator=Paginator(properties,3)
    page=request.GET.get('page')
    paged_properties=paginator.get_page(page)

    return render(request,'properties/properties_list.html',{
        "properties":properties,
    })

def property(request,property_id):
    property=get_object_or_404(Property,pk=property_id)

    return render(request,'properties/property.html',{
        "property":property
    })


@login_required(login_url='login')
def upload(request):
    if request.method=='POST':
        form =PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.FILES["photo_main"])
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
                # sqft=form.cleaned_data['sqft'],
                lot_size=form.cleaned_data['lot_size'],
                photo_main=request.FILES["photo_main"],
                photo_1=request.FILES["photo_1"],
                photo_2=request.FILES["photo_2"],
                photo_3=request.FILES["photo_3"],
                photo_4=request.FILES["photo_4"]
            )
            property.save()
            return redirect('dashboard')
    else:
        form =PropertyForm()
    return render(request,'properties/upload_form.html',{
        "form":form,
    })

def search(request):
    properties=Property.objects.order_by('-list_date')
    if 'type' in request.GET:
        type=request.GET['type']
        if type:
            properties=properties.filter(type__iexact=type)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            properties=properties.filter(city__iexact=city)
    if 'locality'in request.GET:
        locality=request.GET['locality']
        if locality:
            properties=properties.filter(Q(title__icontains=locality) | Q(address__icontains=locality))
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        if min_price:
            properties=properties.filter(price__gte=int(min_price))

    if 'max_price' in request.GET:
        max_price=request.GET['max_price']
        if max_price:
            properties=properties.filter(price__lte=max_price)
    
    if 'available' in request.GET:
        available=request.GET['available']
        if available:
            properties=properties.filter(availibility__exact=available)

    if 'furnishing' in request.GET:
        furnishing=request.GET['furnishing']
        if furnishing:
            properties=properties.filter(furnishing__exact=furnishing)
    
    if 'bathroom' in request.GET:
        bathroom=request.GET['bathroom']
        if bathroom:
            properties=properties.filter(bathroom__exact=bathroom)
    
    # if 'furnishing' in request.GET:
    #     furnishing=request.GET['furnishing']
    #     if furnishing:
    #         properties=properties.filter(furnishing__exact=furnishing)

    return render(request,'properties/search.html',
    {
        "properties":properties,
        "state_list":state_list,
        "type":type,
        "fursnished":fursnished,
        "apartment_type":apartment_type,
        "availibility":availibility,
        "entries":request.GET,
    })

