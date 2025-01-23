from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import YogaClass, Booking
from .forms import BookingForm

# Create your views here.

def classes(request):
    yoga_classes = YogaClass.objects.all()
    return render(request, 'classes.html', {'yoga_classes': yoga_classes})

def booking(request):
    return render(request, 'booking.html')

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
    return render(request, 'booking.html', {'form': form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})