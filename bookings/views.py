from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date, timedelta
from .models import YogaClass, Booking, ClassSchedule
from .forms import BookingForm

def classes(request):
    yoga_classes = YogaClass.objects.all()
    return render(request, 'classes.html', {'yoga_classes': yoga_classes})

# Books a class
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
        yoga_classes = YogaClass.objects.all()
        form = BookingForm()
    return render(request, 'book_a_class.html', {'form': form, 'yoga_classes': yoga_classes})


# Display user's bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('class_schedule', 'class_schedule__yoga_class')
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        class_schedule_id = request.POST.get('class_schedule')
        class_schedule = get_object_or_404(ClassSchedule, id=class_schedule_id)
        booking.booking_date = booking_date
        booking.class_schedule = class_schedule
        booking.save()
        return redirect('my_bookings')
    return render(request, 'my_bookings.html')

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')
    return redirect('my_bookings')

# Returns class schedules for a given class
def get_class_schedules(request, class_id):
    if request.method == 'GET':
        schedules = ClassSchedule.objects.filter(yoga_class_id=class_id)
        schedule_data = [
            {
                'id': schedule.id,
                'day_of_week': schedule.day_of_week,
                'start_time': schedule.start_time.strftime('%H:%M'),
            } for schedule in schedules
        ]
        return JsonResponse({'schedules': schedule_data})

# Returns valid booking dates
def get_valid_dates(request):
    if request.method == 'GET':
        today = date.today()
        dates = [
            (today + timedelta(days=i)).strftime('%Y-%m-%d')
            for i in range(28)  # Next 4 weeks
        ]
        return JsonResponse({'dates': dates})