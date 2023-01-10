from django.shortcuts import render
from django.views import View, generic
from .models import Booking


class Home(generic.ListView):
    model = Booking
    template_name = 'index.html'