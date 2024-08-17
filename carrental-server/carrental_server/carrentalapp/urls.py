from django.urls import path
from .views import (
    VehicleApiView,
    AvailableVehicleApiView,
    BookingApiView
)

# End points for adding new Vehicles, new Bookings and list of available Vehicles
urlpatterns = [
    path('vehicle/', VehicleApiView.as_view()),
    path('bookings/', BookingApiView.as_view()),
    path('available-vehicle/', AvailableVehicleApiView.as_view())
]