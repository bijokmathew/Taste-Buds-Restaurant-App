from django.shortcuts import render, redirect
from django.views import View, generic
from .models import Booking
from .forms import BookingForm


class Home(generic.ListView):
    model = Booking
    template_name = 'index.html'


def reserve_table(request): 
    """
    * reserve_table method is used for booking the table
    * If user select the booking table option then it goes to
      booking form and user can update the required info.
    * If user select submit on booking form then it saves the 
      data to the booking model and redirect to bookinglist 
    """
    if request.method == 'GET':
        context = {
            'booking_from': BookingForm()
        }
        return render(request, 'booking.html', context=context)
    elif request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            # To avoid Null constraint violation when saving object w
            # ith Foreign Key relationships
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('home')
    
