from django.shortcuts import render
from property.dictionaries import type,fursnished,apartment_type,availibility,state_list
from property.models import Property

def homepage(request):
    latest_properties=Property.objects.order_by('-list_date').filter(published=True)[:4]
    return render(request,'pages/homepage.html',
        {
            "latest_properties":latest_properties,
            "state_list":state_list,
            "type":type,
            "fursnished":fursnished,
            "apartment_type":apartment_type,
            "availibility":availibility,
            "entries":request.GET,
        }
    )
def about(request):
    return render(request,'pages/about.html')
