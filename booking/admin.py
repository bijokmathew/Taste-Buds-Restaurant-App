from django.contrib import admin
from .models import Booking, Contact

# Registering Book model in to admin panel


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    BookingAdmin class do the following customization
    * By usining decorative funtion register 'Booking' model
      with admin
    * Added filter function in the admin panel so that admin can
      filter the list based on the given options
    * Added search option in the admin panel which help to search
      booking based on the search item
    * Added the list of field of Booking model which has to display on the
      admin panel
    * Defined accept_booking and decline_booking for confirming or rejectiong
      the booking
    """
    list_display = ('user', 'name', 'booked_date', 'booked_time',
                    'number_guest', 'booking_status')
    list_filter = ('booked_date', 'booking_status', 'booked_time', 'user')
    search_fields = ('name', 'booked_time', 'number_guest')
    actions = ['accept_booking', 'decline_booking']

    def accept_booking(self, request, queryset):
        """
        Admin can approve the booking and update the booking_status
        in to 1
        """
        queryset.update(booking_status=1)

    def decline_booking(self, request, queryset):
        """
        Admin can decline the booking and update the booking_status
        in to 2
        """
        queryset.update(booking_status=2)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    ContactAdmin class do the following customization
    * By usining decorative funtion register 'Contact' model
      with admin
    * Added filter function in the admin panel so that admin can
      filter the message list based on the given options
    * Added search option in the admin panel which help to search
      messages based on the search item
    * Added the list of fields of contact models which has to display on 
      the admin panel
    """
    list_display = ('name', 'subject', 'message', 'email')
    list_filter = ('subject', 'name')
    search_fields = ('name', 'subject')
