from django.urls import path

from . import views

urlpatterns = [
  # path('<int:property_id>', views.contacts, name='contacts'),
  path('contact', views.contact, name='contact'),
]