from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# Create your views here

class CustomUserCreate(APIView):
    """
    API View for user creation.
    Permission classes is set to 'AllowAny' as there is no validation done here.
    """
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        """
        Gets new user data from the post request and serializes the data.
        Register the new user if serialization is valid.
        """
        print(request.data)
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    """
    API View for blacklisting tokens when user clicks on the log out button.
    Permission class is set to 'AllowAny' as there is no validation done here.
    """
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        """
        Gets the refresh token when user clicks on the log out button and
        puts the refresh token into the black list so that it cannot be reused.
        """
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)