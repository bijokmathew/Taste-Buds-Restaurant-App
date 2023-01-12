from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    """
    This class overrides forms's DateInput class
    member input_type in to date type so that we can
    use this type in the booking form
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    BookingForm class is created by inheriting Django Modelform.
    And pass the booking Model and the required model fields which need to
    display on the template. This BookingForm class hekp to populate the model
    fields on the booking form template
    """
    
    class Meta:
        model = Booking
        fields = '__all__'

        exclude = ('user', 'booking_status')
        widgets = {
                    'booked_date': DateInput()
                }                
