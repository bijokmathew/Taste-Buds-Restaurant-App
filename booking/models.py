from django.db import models
from django.contrib.auth.models import User

# tuple is used to hold the status of booking
# 0 --> Pending
# 1 --> approved
# 2 --> declined
BOOKING_STATUS = ((0, 'pending'), (1, 'approved'), (2, 'declined'))

# tuple is used to store booking times and this is used to display as dropdown
# list in the booking form
# Business hours of retaurant : 11 to 23

TIME = (
    ('11.00', '11.00'),
    ('11.30', '11.30'),
    ('12.00', '12.00'),
    ('12.30', '12.30'),
    ('13.00', '13.00'),
    ('13.30', '13.30'),
    ('14.00', '14.00'),
    ('14.30', '14.30'),
    ('15.00', '15.00'),
    ('15.30', '15.30'),
    ('16.00', '16.00'),
    ('16.30', '16.30'),
    ('17.00', '17.00'),
    ('17.30', '17.30'),
    ('18.00', '18.00'),
    ('18.30', '18.30'),
    ('19.00', '19.00'),
    ('19.30', '19.30'),
    ('20.00', '20.00'),
    ('20.30', '20.30'),
    ('21.00', '21.00'),
    ('21.30', '21.30'),
    ('22.00', '22.00'),
    ('22.30', '22.30'),
)   
# tuple is used to store the number of guest and and this is used to display 
# as dropdown list in the booking form

GUEST = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
)


class Booking(models.Model):
    """
    Booking table stores the name, email, number of guest
    date and time of booking in to the postgresql db.
    By default the booking status is 'pending'and
    this is controlled by the field 'status' in the table

    Booking table is sorted according the descending order of booking
    date and the magic method return name, date and time of booking

    """
    user = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name='table_booking')
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    booked_date = models.DateField(blank=False)
    booked_time = models.CharField(
                    max_length=50, default='19:30', choices=TIME)
    number_guest = models.PositiveIntegerField(choices=GUEST, default=2)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    
    class Meta:
        ordering = ['-booked_date']

        # To ensures same user can only be booked once for each date.
        # Avoid double booking
        constraints = [
            models.UniqueConstraint(
                fields=['booked_date', 'booked_time'], name='unique_booking'),
        ]

    def __str__(self):
        return f"Booked the table on {self.booked_date} {self.booked_time}\
                by {self.name}"
