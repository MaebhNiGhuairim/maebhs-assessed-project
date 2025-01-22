from django.db import models
from django.contrib.auth.models import User

class YogaClass(models.Model):
    class_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.class_name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yoga_class = models.ForeignKey(YogaClass, on_delete=models.CASCADE)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.yoga_class.class_name} on {self.booking_date}"