from .models import Booking
from django import forms
from .widget import DateInput
from .models import TIME, GUEST
from . import validator
from django.core.exceptions import NON_FIELD_ERRORS


class BookingForm(forms.ModelForm):
    """
    BookingForm class is created by inheriting Django Modelform.
    And pass the booking Model and the required model fields which need to
    display on the template.Also added label, placeholder and validation to
    the feilds.This BookingForm class help to populate the model fields on
    the booking form template.
    """

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
    )

    email = forms.EmailField(
            label='E-Mail (Optinal)',
            widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}),
    )

    booked_time = forms.CharField(
        label='Arrival Time',
        max_length=50,
        required=True,
        widget=forms.Select(choices=TIME)
    )

    booked_date = forms.DateField(
        label='Date of Booking',
        required=True,
        validators=[validator.validate_future_date],
        error_messages={'invalid': 'Date is not valid. Please select a\
        future date !!!'},
        widget=DateInput()
    )

    number_guest = forms.IntegerField(
        label='Number Of Guests',
        required=True,
        widget=forms.Select(choices=GUEST)
    )

    class Meta:
        model = Booking
        fields = '__all__'

        exclude = ('user', 'booking_status')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': 'Invalid, incorrect info or double booking',
            }
        }
        widgets = {
                    'booked_date': DateInput()
        }
