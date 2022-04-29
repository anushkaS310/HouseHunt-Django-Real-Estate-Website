from django.urls import path
from . import views
urlpatterns=[
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('db_upload',views.db_upload,name="db_upload"),
    path('db_bookmark',views.db_bookmark,name="db_bookmark"),
    path('logout',views.logout,name="logout"),
]