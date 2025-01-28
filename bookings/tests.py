from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import YogaClass, ClassSchedule, Booking
from django.db import IntegrityError
from django.core.exceptions import ValidationError

class YogaClassTests(TestCase):
    """Tests for the YogaClass model"""
    
    def setUp(self):
        # Create a test yoga class
        self.yoga_class = YogaClass.objects.create(
            class_name="Beginner Yoga",
            description="A gentle introduction to yoga",
            duration=timedelta(minutes=60)
        )

    def test_yoga_class_creation(self):
        """Test that a yoga class can be created"""
        self.assertEqual(self.yoga_class.class_name, "Beginner Yoga")
        self.assertEqual(self.yoga_class.duration, timedelta(minutes=60))

class ClassScheduleTests(TestCase):
    """Tests for the ClassSchedule model"""
    
    def setUp(self):
        # Create test data
        self.yoga_class = YogaClass.objects.create(
            class_name="Beginner Yoga",
            description="A gentle introduction to yoga",
            duration=timedelta(minutes=60)
        )
        self.schedule = ClassSchedule.objects.create(
            yoga_class=self.yoga_class,
            day_of_week="Monday",
            start_time="09:00"
        )

    def test_schedule_creation(self):
        """Test that a class schedule can be created"""
        self.assertEqual(self.schedule.day_of_week, "Monday")
        self.assertEqual(self.schedule.start_time, "09:00")

class BookingSystemTests(TestCase):
    """Test cases for the booking system"""
    
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test yoga class
        self.yoga_class = YogaClass.objects.create(
            class_name="Test Yoga",
            description="Test description",
            duration=timedelta(minutes=60)
        )
        
        # Create test schedule
        self.schedule = ClassSchedule.objects.create(
            yoga_class=self.yoga_class,
            day_of_week="Monday",
            start_time="09:00"
        )
        
        self.client = Client()
        self.client.login(username='testuser', password='testpass123')

    def test_booking_page_loads(self):
        """Test that booking page loads with available classes"""
        response = self.client.get(reverse('book_a_class'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.yoga_class.class_name)
    
    def test_successful_booking(self):
        """Test that a user can successfully book a class"""
        # Get tomorrow's date
        tomorrow = datetime.now().date() + timedelta(days=1)
        # Ensure tomorrow is a Monday (same as schedule's day_of_week)
        while tomorrow.strftime('%A') != self.schedule.day_of_week:
            tomorrow += timedelta(days=1)

        # Create the booking
        booking = Booking.objects.create(
            user=self.user,
            class_schedule=self.schedule,
            booking_date=tomorrow
        )
        
        # Verify booking was created
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.class_schedule, self.schedule)
        self.assertEqual(booking.booking_date, tomorrow)
    
    def test_view_my_bookings(self):
        """Test that user can view their bookings"""
        # Get tomorrow's date
        tomorrow = datetime.now().date() + timedelta(days=1)
        # Ensure tomorrow is a Monday (same as schedule's day_of_week)
        while tomorrow.strftime('%A') != self.schedule.day_of_week:
            tomorrow += timedelta(days=1)

        # Create a booking
        Booking.objects.create(
            user=self.user,
            class_schedule=self.schedule,
            booking_date=tomorrow
        )
        
        # Check my bookings page
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.yoga_class.class_name)
    
    def test_anonymous_user_redirect(self):
        """Test that anonymous users are redirected to login"""
        self.client.logout()
        response = self.client.get(reverse('book_a_class'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

class BookingModelTests(TestCase):
    """Tests for the Booking model"""
    
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Create test yoga class and schedule
        self.yoga_class = YogaClass.objects.create(
            class_name="Beginner Yoga",
            description="A gentle introduction to yoga",
            duration=timedelta(minutes=60)
        )
        self.schedule = ClassSchedule.objects.create(
            yoga_class=self.yoga_class,
            day_of_week="Monday",
            start_time="09:00"
        )

    def test_booking_creation(self):
        """Test that a booking can be created"""
        booking = Booking.objects.create(
            user=self.user,
            class_schedule=self.schedule,
            booking_date=datetime.now().date()
        )
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.class_schedule, self.schedule)

    def test_duplicate_booking_prevention(self):
        """Test that duplicate bookings are not allowed"""
        # Create first booking
        booking1 = Booking.objects.create(
            user=self.user,
            class_schedule=self.schedule,
            booking_date=datetime.now().date()
        )
        
        # Try to create duplicate booking for same user, class, and date
        with self.assertRaises(ValidationError):
            booking2 = Booking(
                user=self.user,
                class_schedule=self.schedule,
                booking_date=booking1.booking_date
            )
            booking2.full_clean()
            booking2.save()

    def test_duplicate_booking_prevention_on_edit(self):
        """Test that editing a booking cannot create a duplicate"""
        date1 = datetime.now().date()
        date2 = date1 + timedelta(days=1)
        
        # Create two separate bookings on different dates
        booking1 = Booking.objects.create(
            user=self.user,
            class_schedule=self.schedule,
            booking_date=date1
        )
        
        booking2 = Booking.objects.create(
            user=self.user,
            class_schedule=self.schedule,
            booking_date=date2
        )
        
        # Try to edit booking2 to have the same date as booking1
        with self.assertRaises(ValidationError):
            booking2.booking_date = date1
            booking2.full_clean()
            booking2.save()
