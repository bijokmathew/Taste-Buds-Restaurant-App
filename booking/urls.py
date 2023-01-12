from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('booking/', views.reserve_table, name='booking'),
    path('mybooking/', views.MyBooking.as_view(), name='mybooking')
]

