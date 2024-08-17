import uuid
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

# class Customer(models.Model):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=20)
#     middle_name = models.CharField(max_length=50, blank=True)
#     last_name = models.CharField(max_length=50)
#     license_number = models.CharField(max_length=50, blank=False)
#     date_of_birth = models.DateField(null=True)
#     phone_number = models.CharField(max_length=50)
#     address = models.CharField(max_length=150, blank=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

class Vehicle(models.Model):
    """
    Defines a Vehicle class.
    """
    plate_num = models.CharField(max_length=10, primary_key=True)
    vehicle_make = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)
    built_year = models.IntegerField()
    color = models.CharField(max_length=20)
    vehicle_class = models.CharField(max_length=20)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField()

class Booking(models.Model):
    """
    Defines a Booking class.
    A Booking is deleted when the corresponding User is deleted.
    A Booking is deleted when the corresponding Vehicle is deleted.
    """
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking_date = models.DateField(default=timezone.now)

    class BookingStatus(models.TextChoices):
        BOOKED = 'Booked'
        CANCELLED = 'Cancelled'
        IN_PROGRESS = 'In Progress'
        COMPLETED = 'Completed'
        OVERDUE = 'Overdue'

    booking_status = models.CharField(choices=BookingStatus.choices, default=BookingStatus.BOOKED, max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    final_cost = models.DecimalField(max_digits=9, decimal_places=2)
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plate_num = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class PaymentDetails(models.Model):
    """
    Defines a PaymentDetails class.
    A PaymentDetails is deleted when the corresponding User is deleted.
    """
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    routing_number = models.CharField(max_length=9)
    account_number = models.CharField(max_length=20)
    card_expiry = models.DateField()
    billing_address = models.CharField(max_length=256, blank=True)
    account_name = models.CharField(max_length=256, blank=True)
