from django import forms
from .models import Booking, ClassSchedule

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['class_schedule', 'booking_date']

    # Dynamically populate the dropdown with available schedules
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_schedule'].queryset = ClassSchedule.objects.all()