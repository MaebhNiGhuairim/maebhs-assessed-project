from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import YogaClass, Booking, ClassSchedule
from .forms import BookingForm

def classes(request):
    yoga_classes = YogaClass.objects.all()
    return render(request, 'classes.html', {'yoga_classes': yoga_classes})

# Books a class
@login_required
def book_class(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm(user=request.user)
    
    return render(request, 'book_a_class.html', {
        'form': form
    })


# Display user's bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('class_schedule', 'class_schedule__yoga_class')
    return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        # Simple date update only
        new_date = request.POST.get('booking_date')
        booking.booking_date = new_date
        booking.save()
        return redirect('my_bookings')
    
    # Get valid dates for this booking's existing class schedule
    schedule = booking.class_schedule
    today = datetime.today()
    valid_dates = []
    
    # Generate next 4 valid dates based on the schedule's day
    for i in range(0, 28):
        date = today + timedelta(days=i)
        if date.strftime('%A') == schedule.day_of_week:
            valid_dates.append(date)
    
    return render(request, 'edit_booking.html', {
        'booking': booking,
        'valid_dates': valid_dates,
    })

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')
    return redirect('my_bookings')

# Returns class schedules for a given class
@login_required
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
    schedule_id = request.GET.get('schedule_id')
    if not schedule_id:
        return JsonResponse({'dates': []})
    
    schedule = get_object_or_404(ClassSchedule, id=schedule_id)
    today = datetime.today()
    dates = []
    
    # Get next 4 weeks of valid dates
    for i in range(28):
        date = today + timedelta(days=i)
        if date.strftime('%A') == schedule.day_of_week:
            dates.append(date.strftime('%Y-%m-%d'))
    
    return JsonResponse({'dates': dates})

