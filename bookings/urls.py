# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),  # Display available classes
    path('book-class/', views.book_class,
         name='book_a_class'),  # Book a class
    path('my-bookings/', views.my_bookings,
         name='my_bookings'),  # View user's bookings
    path('edit_booking/<int:booking_id>/', views.edit_booking,
         name='edit_booking'),  # Edit a booking
    path('delete-booking/<int:booking_id>/', views.delete_booking,
         name='delete_booking'),  # Delete a booking
    path('api/schedules/<int:class_id>/', views.get_class_schedules,
         name='get_class_schedules'),  # Get class schedules
    path('api/valid-dates/', views.get_valid_dates,
         name='get_valid_dates'),  # Get valid booking dates

]