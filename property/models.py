import datetime
from django.db import models


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
type=(
    ("1","Sell"),
    ("2","Rent"),
)
  
class Property(models.Model):
    user_id=models.IntegerField(models.ForeignKey("User", on_delete=models.CASCADE))
    # user_name=models.CharField(models.ForeignKey("User", on_delete=models.CASCADE),max_length=150)
    type=models.CharField(max_length=20,choices= type,default="Sell")
    published=models.BooleanField(default=True)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20,choices= state_list)
    zipcode=models.CharField(max_length=20)
    description=models.TextField()
    price=models.IntegerField()
    availibility=models.CharField(max_length=20,choices=availibility)
    bathroom=models.IntegerField()
    garage=models.BooleanField(null=True)
    gym=models.BooleanField(null=True)
    swimming_pool=models.BooleanField(null=True)
    furnishing=models.CharField(null=True,max_length=20,choices=fursnished)
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=1)
    # list_date=models.DateTimeField(default=datetime.now,blank=True)
    # photo_main=forms.ImageField(upload_to='photos/
    # %Y/%m/%d')
    # photo_1=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    # photo_2=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    # photo_3=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    


from django.db import models

# Create your models here.
