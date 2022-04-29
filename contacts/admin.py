from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','property','email')
    search_field=('name','property','email')
admin.site.register(Contact,ContactAdmin)