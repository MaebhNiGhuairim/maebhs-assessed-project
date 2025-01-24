from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),  # Display available classes
    path('api/schedules/<int:class_id>/', views.get_class_schedules, name='get_class_schedules'), 
    path('api/valid-dates/', views.get_valid_dates, name='get_valid_dates'),
    path('book-class/', views.book_class, name='book_class'),  # Book a class
    path('my-bookings/', views.my_bookings, name='my_bookings'),  # View user's bookings
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit-booking'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete-booking'),
]