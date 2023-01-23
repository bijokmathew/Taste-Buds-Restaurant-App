from .models import Booking, Contact
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


class ContactForm(forms.ModelForm):
    """
    ContactForm class is created by inheriting Django Modelform.
    And pass the Contact Model and all the model fields to display 
    on the template.Also removed label and add placeholder and style
    attributes to the feilds.This ContactForm class help to populate 
    the contact model fields on the contact form template.
    """
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': "Your Name", 'class': 'form-control'}
            )
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Your Email', 'class': 'form-control'}
        )
    )
    subject = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Subject', 'class': 'form-control'}
        )
    )
    message = forms.CharField(
        label='',
        max_length=300,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message', 'class': 'form-control', 'rows': '5'
                }
        )
    )

    class Meta:
        model = Contact
        fields = '__all__'
