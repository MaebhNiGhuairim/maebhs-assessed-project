# Generated by Django 4.2.18 on 2025-01-23 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_classschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='yoga_class',
        ),
        migrations.AddField(
            model_name='booking',
            name='class_schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.classschedule'),
        ),
    ]
