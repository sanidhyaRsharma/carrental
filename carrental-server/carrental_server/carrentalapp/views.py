from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Vehicle, Booking, PaymentDetails
from django.apps import apps
from .serializers import VehicleSerializer, BookingSerializer, PaymentDetailsSerializer
from django.utils.dateparse import parse_datetime
from django.utils import timezone


class VehicleApiView(APIView):
    """
    API View for Vehicle class
    """
    def get(self, request, *args, **kwargs):
        """
        Returns details of a Vehicle based on given parameters.
        """
        vehicles = Vehicle.objects.filter(is_active=True)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Gets new Vehicle data from the post request and serializes the data.
        Adds the new Vehicle to databse if serialization is valid.
        """
        data = {
            'plate_num': request.data.get('plate_num'),
            'vehicle_make': request.data.get('vehicle_make'),
            'vehicle_model': request.data.get('vehicle_model'),
            'built_year': request.data.get('built_year'),
            'color': request.data.get('color'),
            'vehicle_class': request.data.get('vehicle_class'),
            'price_per_day': request.data.get('price_per_day'),
            'is_active': request.data.get('is_active')
        }

        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvailableVehicleApiView(APIView):
    """
    API View for available Vehicles
    """
    def post(self, request, *args, **kwargs):
        """
        Shows the list of available Vehicles for a given start and end time.
        """
        bookings = Booking.objects.all()
        vehicles = Vehicle.objects.filter(is_active=True)
        available_vehicles = []
        start_time = timezone.make_aware(parse_datetime(request.data.get('start_time')))
        end_time = timezone.make_aware(parse_datetime(request.data.get('end_time')))
        for vehicle in vehicles:
            booked_before = False
            for booking in bookings:
                if vehicle.plate_num == booking.plate_num.plate_num:
                    if (booking.start_time < start_time and booking.end_time < start_time)\
                            or (booking.start_time > end_time and booking.end_time > end_time):
                        available_vehicles.append(vehicle)
                    print('Booked before ' + vehicle.plate_num)
                    booked_before = True
            if not booked_before:
                available_vehicles.append(vehicle)
        print(available_vehicles)
        serializer = VehicleSerializer(available_vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookingApiView(APIView):
    """
    API View for Booking.
    """
    def get(self, request, *args, **kwargs):
        """
        Returns details of a booking.
        """
        bookings = Booking.objects
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Gets booking data from the post request and serializes the data.
        Cost of booking is calculated at this point.
        Add the new Booking if serialization is valid.
        """
        customer = apps.get_model('users', 'NewUser').objects.filter(email=request.data.get('email')).first()
        vehicle = Vehicle.objects.filter(plate_num=request.data.get('plate_num')).first()
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        data = {
            'booking_date': request.data.get('booking_date'),
            'start_time': start_time,
            'end_time': end_time,
            'customer_id': customer.pk,
            'plate_num': vehicle.pk,
            'final_cost': int((parse_datetime(end_time) - parse_datetime(start_time)).days)*vehicle.price_per_day
        }

        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)