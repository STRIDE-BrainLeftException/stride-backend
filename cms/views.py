from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken

from cms.models import Booking


class GalactiveUserLoginView(APIView):
    def post(self, request):
        print(request.data)
        galactic_id = request.data.get("galactic_id")

        user = authenticate(request, token=galactic_id)
        if user is None:
            return Response({"error": "Invalid Credentials"}, status=400)

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=200,
        )


class PriceCalculationView(APIView):
    def post(self, request):
        start_planet_id = request.data.get("start_planet_id")
        end_planet_id = request.data.get("end_planet_id")
        ship_type_id = request.data.get("ship_type_id")
        package_id = request.data.get("package_id")
        seat_count = request.data.get("seat_count")

        try:
            booking = Booking(
                start_planet_id=start_planet_id,
                end_planet_id=end_planet_id,
                ship_type_id=ship_type_id,
                package_id=package_id,
                seat_count=seat_count,
            )
            return Response(
                {
                    "total": booking.total_price,
                    "calculated_price": booking.calculated_price,
                    "tax": booking.tax_price,
                },
                status=200,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=400)
