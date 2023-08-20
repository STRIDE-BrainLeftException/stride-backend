from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken


class GalactiveUserLoginView(APIView):
    def post(self, request):
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
