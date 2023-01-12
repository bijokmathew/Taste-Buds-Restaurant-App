from django.shortcuts import render
from django.views import View, generic
from .models import Booking
from .forms import BookingForm


class Home(generic.ListView):
    model = Booking
    template_name = 'index.html'


def reserve_table(request):
    context = {
        'booking_from': BookingForm()
    }
    return render(request, 'booking.html', context=context)
