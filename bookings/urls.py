from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('book/', views.book_class, name='book_class'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]