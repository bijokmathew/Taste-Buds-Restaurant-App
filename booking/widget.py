from django import forms


class DateInput(forms.DateInput):
    """
    This class overrides forms's DateInput class
    member input_type in to date type so that we can
    use this type in the booking form
    """
    input_type = 'date'
