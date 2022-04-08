from datetime import  datetime
from distutils.command.upload import upload
from property.dictionaries import type,fursnished,apartment_type,availibility,state_list
from django import forms

# type=(
#     ("1","Sell"),
#     ("2","Rent"),
# )
# state_list=(
#     ("1","Andhra Pradesh"),
#     ("2","Arunachal Pradesh"),
#     ("3","Uttar Pradesh"),
#     ("4","Delhi"))

# apartment_type=(
#     ("1","1RK"),
#     ("2","1BHK"),
#     ("3","2BHK"),
#     ("4","3BHK"),
#     ("5","4BHK"),
#     ("6","4BHK"),
# )
# fursnished=(
#     ("1","Fully Furnished"),
#     ("2","Semi Furnished"),
#     ("3","Unfurnished"),

# )
# availibility=(
#     ("1","Immediately"),
#     ("2","In 15 days"),
#     ("3","In a month"),
# )

  
class PropertyForm(forms.Form):
    type=forms.ChoiceField(choices=type)
    title=forms.CharField(max_length=200)
    address=forms.CharField(max_length=20)
    city=forms.CharField(max_length=20)
    state=forms.ChoiceField(choices= state_list)
    zipcode=forms.CharField(max_length=6,min_length=6)
    description=forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 60}))
    price=forms.IntegerField()
    apartment_type=forms.ChoiceField(choices=apartment_type)
    availibility=forms.ChoiceField(choices=availibility)
    bathroom=forms.IntegerField(min_value=0,max_value=10)
    garage=forms.BooleanField(required=False)
    gym=forms.BooleanField(required=False)
    swimming_pool=forms.BooleanField(required=False)
    furnishing=forms.ChoiceField(label="Furnishing Status",choices=fursnished)
    # sqft=forms.IntegerField(label="Carpet Area(in sqfts)",min_value=100)
    lot_size=forms.DecimalField(label="Lot Size (int sqfts)",max_digits=6,decimal_places=1,min_value=100)
    # list_date=forms.DateTimeField(default=datetime.now,blank=True)
    photo_main=forms.ImageField(required=False)
    photo_1=forms.ImageField(required=False)
    photo_2=forms.ImageField(required=False)
    photo_3=forms.ImageField(required=False)
    photo_4=forms.ImageField(required=False)
    


