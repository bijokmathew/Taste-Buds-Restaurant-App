from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.exceptions import ValidationError
from .forms import BookingForm, ContactForm
from django.views import View, generic
from django.contrib import messages
from .models import Booking
import datetime
import json


class Home(generic.ListView):
    """
    Home is class-based view.This model used to display the homepage
    by selecting the restaurant web url.Get method handle the get
    request from url.py and launch the homepage.Homepage has contact
    form, for populating the contact model fields used modelForm.
    Post method is used to submit the contact fields data by using
    contat model form and saved in to contact model
    """
    def get(self, request):
        galleryDatas = []
        chefsInfo = []
        model = Booking
        # take the image urls for Gallery section from the 
        # gallery_data.json file present in data folder
        with open("data/gallery_data.json", "r") as json_data:
            galleryDatas = json.load(json_data)
        # Take the chef details for chefs section from the
        # chefs_details.json file present in data folder
        with open("data/chefs_details.json", "r") as chef_json_data:
            chefsInfo = json.load(chef_json_data)
        template_name = 'index.html'
        context = {
            'galleryDatas': galleryDatas,
            'chefsInfo': chefsInfo,
            'contactForm': ContactForm()
        }
        return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):
        # Take the user filled datas from contact form
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print("form is valid and save")
            form.save()
            messages.success(request, "Your message has been sent. Thank you!")
            return redirect('home')
        else:
            messages.error(request, "Invalid entry, please fill the form with\
                 correct data")


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
            'booking_form': BookingForm()
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
            messages.success(
                request, "Your request has been submitted. Thank you!"
                )
            return redirect('mybooking')
        else:
            # To show the filed validation error like double booking,
            # invalid date etc
            show_form_errormsg(form, request)
            context = {
                'booking_form': form
            }
            return render(
                request, 'booking.html', context=context
            )


class MyBooking(generic.ListView):
    """
    Mybooking function display all booking of the autherized user.
    Allow the customer to edit or cancel his booking.Also it check
    the booking date so that this will display.This function derived
    from generic ListView and use Booking model for fetching the booking
    details.By using filter and check_valid_datetime functions, filter valid
    booked date and booked time records from the booking model

    """
    model = Booking
    template_name = 'mybooking.html'
    now = datetime.datetime.now()

    def check_valid_datetime(self, mybooking):
        """
        check_valid_datetime function used to check the booked_time and booked
        date in my booking list is a valid by comparing the booked date and
        booked time with today date and time. if booked date and booked_time is
        same or future date and time then the function return true, else
        return false.

        """
        current_date = datetime.date.today()
        current_date_time = datetime.datetime.today()
        current_time = current_date_time.strftime("%H:%M")
        if mybooking.booked_date == current_date and \
           mybooking.booked_time >= current_time:
            return True
        elif mybooking.booked_date > current_date:
            return True
        else:
            return False

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Fetch only current user booking from nooking model
            booking_list = Booking.objects.filter(user=request.user)
            # validate whether the booking date is expired or not
            valid_booking = filter(self.check_valid_datetime, booking_list)
            context = {
                'bookings': valid_booking
            }
            return render(request, "mybooking.html", context=context)
        else:
            messages.info(
                request, "You have to SignIn first to view the booking status"
            )
            return redirect(reverse('account_login'))


def edit_mybooking(request, booking_id):
    """
    edit_mybooking used to modify the booking details
    ** booking_id : this id passed from the my booking view
    which is used to fetch the booking details from the booking
    model.And pass these details in to the django form(BookingForm)
    which helps to populate the required model fileds with corresponding
    data in to the edit booking template.While updating the booking 
    details, we have to change the booking status to pending.
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
            upated_booking_form = form.save(commit=False)
            upated_booking_form.booking_status = 0
            upated_booking_form.save()
            messages.success(request, "Booking has been updated. Thank you!")
            return redirect('mybooking')
        else:
            # To show the filed validation error like double booking, 
            # invalid date etc
            show_form_errormsg(form, request)
            return render(
                request, 'booking_edit.html', {'booking_form': form}
            )


def show_form_errormsg(form, request):
    """
    show_form_errormsg method used to show the field validation
    error message.This is generic method take form and request
    as function parameter and based on the validation error, send
    customized message to the template by using django message feature.
    """
    if form.non_field_errors():
        messages.error(
            request, "Invalid entry, incorrect info or double booking"
        )
    if form.has_error('booked_date'):
        messages.error(
            request, 'Invalid entry: Date is not valid. Please select \
                a future date !!!'
        )


def delete_mybooking(request, booking_id):
    """
    delete_mybooking() help the user to delete his selected booking
    details.This function fetch the specfic booking record from model
    and delete it. After deleting it redirect to mybooking page.
    This function make sure that the current user can delete only his
    booking.
    """
    booking_detail = get_object_or_404(Booking, id=booking_id)
    if request.user != booking_detail.user:
        messages.error(request, "You are not authorized")
        return redirect("mybooking")
    else:
        booking_detail.delete()
        messages.success(request, 'Booking has been deleted')
        return redirect('mybooking')
