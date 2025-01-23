from django.contrib import admin
from .models import YogaClass, ClassSchedule, Booking

class YogaClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'duration')
    search_fields = ('class_name',)

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('yoga_class', 'day_of_week', 'start_time')
    list_filter = ('day_of_week', 'start_time')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'class_schedule', 'booking_date')
    search_fields = ('user__username', 'yoga_class__class_name')
    list_filter = ('booking_date',)

    def get_yoga_class(self, obj):
        return obj.class_schedule.yoga_class.class_name
    get_yoga_class.short_description = 'Yoga Class'

admin.site.register(YogaClass, YogaClassAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(ClassSchedule, ClassScheduleAdmin)