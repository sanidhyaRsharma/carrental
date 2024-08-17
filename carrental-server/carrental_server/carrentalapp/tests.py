from django.test import TestCase
from models import Vehicle, Booking, PaymentDetails
# Create your tests here.

class VehicleTestCase(TestCase):
    def setUp(self):
        Vehicle.objects.create(plate_num="TEST_PLATE_NUM", is_active=True, vehicle_make="Porsche", vehicle_model="911")
        Vehicle.objects.create(plate_num="TEST_PLATE_NUM", is_active=True, vehicle_make="Chevrolet", vehicle_model="Malibu")

    def can_get_vehicle(self):
        vehicles = Vehicle.objects.get()
