from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
import json
from .models import Booking
from .forms import BookingForm
from django.core.exceptions import ValidationError


class Home(generic.ListView):

    def get(self, request):
        galleryDatas = []
        chefsInfo = []
        model = Booking
        with open("data/gallery_data.json", "r") as json_data:
            galleryDatas = json.load(json_data)
        template_name = 'index.html'
        with open("data/chefs_details.json", "r") as chef_json_data:
            chefsInfo = json.load(chef_json_data)
        template_name = 'index.html'
        context = {
            'galleryDatas': galleryDatas,
            'chefsInfo': chefsInfo
        }
        return render(request, template_name, context=context)


def reserve_table(request):
    """
    * reserve_table method is used for booking the table
    * If user select the booking table option then it goes to
      booking form and user can update the required info.
    * If user select submit on booking form then it saves the
      data to the booking model and redirect to bookinglist
    * If user has already made booking on same date and same time
      then it should not save to booking model and shows a proper
      message to the user
    """
    if request.method == 'GET':
        context = {
            'booking_from': BookingForm()
        }
        return render(request, 'booking.html', context=context)
    elif request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            # To avoid Null constraint violation when saving object
            # with Foreign Key relationships
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('mybooking')
        else:
            errors = form.errors
            context = {
                'form': form,
                'booking_from': BookingForm()
            }
            return render(
                request, 'booking.html', context=context
            )


class MyBooking(generic.ListView):
    model = Booking
    template_name = 'mybooking.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            booking_list = Booking.objects.filter(user=request.user)
            context = {
                'bookings': booking_list
            }
            return render(request, "mybooking.html", context=context)


def edit_mybooking(request, booking_id):
    """
    edit_mybooking used to modify the booking details
    ** booking_id : this id passed from the my booking view
    which is used to fetch the booking details from the booking
    model.And pass these details in to the django form(BookingForm)
    which helps to populate the required model fileds with corresponding
    data in to the edit booking template
    """
    booking_details = get_object_or_404(Booking, id=booking_id)
    if request.method == 'GET':
        form = BookingForm(instance=booking_details)
        context = {
            'booking_form': form
        }
        return render(request, "booking_edit.html", context=context)
    elif request.method == 'POST':
        form = BookingForm(request.POST, instance=booking_details)
        if form.is_valid():
            form.save()
            return redirect('mybooking')


def delete_mybooking(request, booking_id):
    """
    delete_mybooking() help the user to delete his selected booking
    details.This function fetch the specfic booking record from model
    and delete it. After deleting it redirect to mybooking page.
    This function make sure that the current user can delete only his
    booking.
    """
    booking_detail = get_object_or_404(Booking, id=booking_id)
    print(booking_detail.user)
    print(request.user)
    if request.user != booking_detail.user:
        return redirect("mybooking")
    booking_detail.delete()
    return redirect('mybooking')
