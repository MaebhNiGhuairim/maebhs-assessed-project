#models.py
from django.db import models
from django.contrib.auth.models import User

class YogaClass(models.Model):
    class_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.class_name
    
class ClassSchedule(models.Model):
    yoga_class = models.ForeignKey(YogaClass, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    start_time = models.TimeField()

    def __str__(self):
        return f"{self.yoga_class.class_name} - {self.day_of_week} at {self.start_time}"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateField()

    class Meta:
        unique_together = ['user', 'class_schedule', 'booking_date']

    def __str__(self):
        return f"{self.user.username} - {self.class_schedule.yoga_class.class_name} on {self.booking_date} at {self.class_schedule.start_time}"
