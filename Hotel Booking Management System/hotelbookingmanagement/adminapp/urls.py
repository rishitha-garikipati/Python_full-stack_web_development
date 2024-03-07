from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('managementhomepage',views.managementhomepage,name='managementhomepage'),
    path('userhomepage',views.userhomepage,name='userhomepage')
]
