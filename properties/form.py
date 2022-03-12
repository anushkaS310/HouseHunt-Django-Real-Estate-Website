from django.db import models
from datetime import date
from distutils.command.upload import upload
from django.db import models
from django import forms
class PropertyForm(forms.Form):
    title=forms.CharField(max_length=200)
    address=forms.CharField(max_length=20)
    city=forms.CharField(max_length=20)
    state=forms.CharField(max_length=20)
    zipcode=forms.CharField(max_length=20)
    description=forms.CharField(widget=forms.Textarea)
    price=forms.IntegerField()
    bedrooms=forms.IntegerField()
    bathroom=forms.DecimalField(max_digits=2,decimal_places=1)
    garage=forms.IntegerField()
    # furnishing=models.Choices()
    sqft=forms.IntegerField()
    is_published=forms.BooleanField()
    lot_size=forms.DecimalField(max_digits=4,decimal_places=1)
    # list_date=forms.DateField(default=date.today)
    # photo_main=forms.ImageField(upload_to='photos/%Y/%m/%d')
    # photo_1=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    # photo_2=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    # photo_3=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    


