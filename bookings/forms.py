from django import forms
from .models import Booking, ClassSchedule

class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': 'dd/mm/yyyy',
                'type': 'text',  # Use 'text' to allow custom date format
            },
            format='%d/%m/%Y'
        ),
        input_formats=[
            '%d/%m/%Y',  # e.g., 02/03/2025
            '%d/%m/%y',  # e.g., 02/03/25
            '%d-%m-%Y',  # e.g., 02-03-2025
            '%d-%m-%y',  # e.g., 02-03-25
            '%d.%m.%Y',  # e.g., 02.03.2025
            '%d.%m.%y',  # e.g., 02.03.25
            '%d %b %Y',  # e.g., 02 Mar 2025
            '%d %b %y',  # e.g., 02 Mar 25
            '%d %B %Y',  # e.g., 02 March 2025
            '%d %B %y',  # e.g., 02 March 25
        ]
    )

    class Meta:
        model = Booking
        fields = ['class_schedule', 'booking_date']

    # Dynamically populate the dropdown with available schedules
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_schedule'].queryset = ClassSchedule.objects.all()