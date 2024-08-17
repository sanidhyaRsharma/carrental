from rest_framework import serializers
from .models import Vehicle, Booking


class VehicleSerializer(serializers.ModelSerializer):
    """
    Serializes a Vehicle.
    Validates data to ensure all required fields are provided.
    """
    class Meta:
        model = Vehicle
        fields = ['plate_num', 'vehicle_make', 'vehicle_model', 'built_year', 'color', 'vehicle_class',
                  'price_per_day', 'is_active']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializes a booking.
    Validates data to ensure all required fields are provided.
    """
    class Meta:
        model = Booking
        fields = ['booking_id', 'start_time', 'end_time', 'final_cost', 'customer_id', 'plate_num']


class PaymentDetailsSerializer(serializers.ModelSerializer):
    """
    Serializes user's payment details.
    Validates data to ensure all required fields are provided.
    """
    class Meta:
        fields = ['customer_id', 'bank_name', 'card_number', 'routing_number', 'account_number', 'card_expiry',
                  'billing_address', 'account_name']