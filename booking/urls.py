from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('booking/', views.reserve_table, name='booking'),
    path('mybooking/', views.MyBooking.as_view(), name='mybooking'),
    path('editbooking/<booking_id>', views.edit_mybooking,
         name='edit_mybooking'),
    path('deletebooking/<booking_id', views.delete_mybooking,
         name='delete_mybooking'),
]

