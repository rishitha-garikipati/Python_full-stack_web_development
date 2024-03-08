from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('userhomepage', views.userhomepage, name='userhomepage'),
    path('bookhotel', views.bookhotel, name='bookhotel'),
    path('contactus', views.contactus, name='contactus'),
]
