from django.urls import path
from . import views
urlpatterns=[
    path("upload",views.upload,name="upload"),
    path('',views.property_list,name="property_list"),
    path('<int:property_id>',views.property,name='property'),
    path('search',views.search,name="search"),
    path('bookmark',views.BookmarkView.as_view(),name="bookmark")
]