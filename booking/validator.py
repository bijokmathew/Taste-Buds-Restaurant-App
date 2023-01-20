from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


def validate_future_date(date):
    """
    This function used to validate the given date is not a
    passed date.We can use this validator check on booking model's
    booked_date field so that we can make sure booking is happening
    for today's or future data. In all other cases, shows an alert to the
    customer to enter valid date
    """
    if date < datetime.date.today():
        raise ValidationError(
            _('%(date)s is not valid, Please select a future date'),
            code='invalid', params={'date': date},
        )
