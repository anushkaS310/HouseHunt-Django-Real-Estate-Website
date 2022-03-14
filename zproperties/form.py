from datetime import  datetime
from distutils.command.upload import upload
from django import forms

type=(
    ("1","Sell"),
    ("2","Rent"),
)
state_list=(
    ("1","Andhra Pradesh"),
    ("2","Delhi"),)

apartment_type=(
    ("1","1RK"),
    ("2","1BHK"),
    ("3","2BHK"),
    ("4","3BHK"),
    ("5","4BHK"),
    ("6","4BHK"),
)
fursnished=(
    ("1","Fully Furnished"),
    ("2","Semi Furnished"),
    ("3","Unfurnished"),

)
availibility=(
    ("1","Immediately"),
    ("2","In 15 days"),
    ("3","In a month"),
)

  
class PropertyForm(forms.Form):
    type=forms.ChoiceField(choices=type)
    title=forms.CharField(max_length=200)
    address=forms.CharField(max_length=20)
    city=forms.CharField(max_length=20)
    state=forms.ChoiceField(choices= state_list)
    zipcode=forms.CharField(max_length=20)
    description=forms.CharField(widget=forms.Textarea)
    price=forms.IntegerField()
    apartment_type=forms.ChoiceField(choices=apartment_type)
    availibility=forms.ChoiceField(choices=availibility)
    bathroom=forms.IntegerField(min_value=0,max_value=10)
    garage=forms.BooleanField(required=False)
    gym=forms.BooleanField(required=False)
    swimming_pool=forms.BooleanField(required=False)
    furnishing=forms.ChoiceField(label="Furnishing Status",choices=fursnished)
    sqft=forms.IntegerField(label="Carpet Area(in sqfts)",min_value=100)
    lot_size=forms.DecimalField(label="Lot Size (int sqfts)",max_digits=4,decimal_places=1,min_value=100)
    # list_date=forms.DateTimeField(default=datetime.now,blank=True)
    # photo_main=forms.ImageField(upload_to='photos/%Y/%m/%d')
    # photo_1=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    # photo_2=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    # photo_3=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    


