from datetime import datetime
from django.db import models

# Create your models here.
class Contact(models.Model):
    property=models.CharField(max_length=200)
    property_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField()
    message=models.TextField()
    contact_date=models.DateTimeField(default=datetime.now)
    user_id=models.IntegerField()
    
