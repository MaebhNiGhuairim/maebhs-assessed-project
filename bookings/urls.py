from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('book-a-class/', views.booking, name='book_a_class'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]