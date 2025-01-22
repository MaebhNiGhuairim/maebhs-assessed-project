from django.contrib import admin
from .models import YogaClass, Booking

class YogaClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'duration')
    search_fields = ('class_name',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'yoga_class', 'booking_date')
    search_fields = ('user__username', 'yoga_class__class_name')
    list_filter = ('booking_date',)

admin.site.register(YogaClass, YogaClassAdmin)
admin.site.register(Booking, BookingAdmin)