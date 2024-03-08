from django.urls import path
from . import views

urlpatterns = [
    path('add_hotel/', views.add_hotel, name='add_hotel'),
    path('view_hotels/', views.view_hotels, name='view_hotels'),
    path("delete_hotel/<int:pk>", views.delete_hotel, name='delete_hotel'),
    path('search/', views.search_view, name='search'),
    path('managementhomepage', views.managementhomepage, name='managementhomepage'),

]
