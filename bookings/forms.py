from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from .models import Booking, ClassSchedule, YogaClass

class BookingForm(forms.ModelForm):
    yoga_class = forms.ModelChoiceField(
        queryset=YogaClass.objects.all(),
        empty_label="Select a class",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'yoga_class'
        })
    )
    
    class_schedule = forms.ModelChoiceField(
        queryset=ClassSchedule.objects.all(),
        empty_label="Select a time",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'class_schedule',
            'disabled': 'disabled'
        })
    )
    
    booking_date = forms.ChoiceField(
        choices=[],  # Will be populated dynamically
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'booking_date',
            'disabled': 'disabled'
        })
    )

    class Meta:
        model = Booking
        fields = ['yoga_class', 'class_schedule', 'booking_date']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Customize display formats
        self.fields['yoga_class'].label_from_instance = lambda obj: f"{obj.class_name}"
        self.fields['class_schedule'].label_from_instance = lambda obj: f"{obj.day_of_week} at {obj.start_time}"

        # Initialize booking_date choices
        self.fields['booking_date'].choices = [('', 'Select a date')]

        # If we have POST data, update the class_schedule queryset
        if self.data.get('yoga_class'):
            self.fields['class_schedule'].queryset = ClassSchedule.objects.filter(
                yoga_class_id=self.data.get('yoga_class')
            )

        # If we have a class_schedule, populate the valid dates
        if self.data.get('class_schedule'):
            schedule = ClassSchedule.objects.filter(id=self.data.get('class_schedule')).first()
            if schedule:
                today = datetime.today()
                dates = []
                # Get next 4 weeks of valid dates
                for i in range(28):
                    date = today + timedelta(days=i)
                    if date.strftime('%A') == schedule.day_of_week:
                        formatted_date = date.strftime('%Y-%m-%d')
                        dates.append((formatted_date, date.strftime('%A, %d %B %Y')))
                self.fields['booking_date'].choices = [('', 'Select a date')] + dates

    def clean(self):
        cleaned_data = super().clean()
        class_schedule = cleaned_data.get('class_schedule')
        booking_date = cleaned_data.get('booking_date')

        if class_schedule and booking_date and self.user:
            try:
                # Convert booking_date string to datetime object
                booking_date = datetime.strptime(booking_date, '%Y-%m-%d').date()
                cleaned_data['booking_date'] = booking_date

                # Check for existing booking
                existing_booking = Booking.objects.filter(
                    user=self.user,
                    class_schedule=class_schedule,
                    booking_date=booking_date
                ).exists()

                if existing_booking:
                    raise ValidationError(
                        f"You have already booked {class_schedule.yoga_class.class_name} "
                        f"on {booking_date.strftime('%d/%m/%Y')}"
                    )

            except ValueError:
                raise ValidationError("Invalid date format")

        return cleaned_data