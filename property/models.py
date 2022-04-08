import datetime
from tkinter import CASCADE
from django.db import models
from datetime import datetime
from property.dictionaries import type,fursnished,apartment_type,availibility,state_list
from django.contrib.auth.models import User

# state_list=(
#     ("1","Andhra Pradesh"),
#     ("2","Arunachal Pradesh"),
#     ("3"," New Delhi"),
#     ("4","Maharashtra"),
#     ("5","Tamil Nadu"),
#     ("6","Uttar Pradesh"),
#     ("7","Uttrakhand"),
#     ("7","Uttrakhand"),)

# apartment_type=(
#     ("1","1RK"),
#     ("2","1BHK"),
#     ("3","2BHK"),
#     ("4","3BHK"),
#     ("5","4BHK"),
#     ("6","5BHK"),
#     ("7","Villa"),
# )
# fursnished=(
#     ("1","Fully Furnished"),
#     ("2","Semi Furnished"),
#     ("3","Unfurnished"),

# )
# availibility=(
#     ("1","Ready to move"),
#     ("2","In 15 days"),
#     ("3","In a month"),
# )
# type=(
#     ("1","Sell"),
#     ("2","Rent"),
# )
  
class Property(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
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
    # sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=1)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d',default='h1.jpg')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d',null=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d',null=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d',null=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d',null=True)

    @property
    def user(self):
        return User.objects.get(pk=self.user_id)
    
