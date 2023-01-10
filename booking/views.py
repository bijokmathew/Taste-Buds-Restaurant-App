from django.shortcuts import render
from django.views import View, generic
from .models import Booking


class base(generic.ListView):
    model = Booking
    template_name = 'base.html'