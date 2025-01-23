from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import YogaClass, Booking, ClassSchedule
from .forms import BookingForm

def classes(request):
    yoga_classes = YogaClass.objects.all()
    return render(request, 'classes.html', {'yoga_classes': yoga_classes})

@login_required
def book_class(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'book_a_class.html', {'form': form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('class_schedule', 'class_schedule__yoga_class')
    return render(request, 'my_bookings.html', {'bookings': bookings})


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_bookings')  # Redirect to a page listing user bookings
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        booking.booking_date = booking_date
        booking.save()
        return redirect('my_bookings')
    return redirect('my_bookings')

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')
    return redirect('my_bookings')