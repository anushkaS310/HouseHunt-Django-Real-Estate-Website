from django.contrib import admin
from .models import Property



class PropertyAdmin(admin.ModelAdmin):
    list_display=('id','uid','published','title','city','state','price')
    list_display_links=('id','uid','title')
    list_filter=('published',)
    list_editable=('published',)
    search_fields=('uid__username','state','price','city','garage')
    list_per_page=10
admin.site.register(Property,PropertyAdmin)
