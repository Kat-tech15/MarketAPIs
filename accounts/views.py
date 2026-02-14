from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, EmptySerializer, MessageSerializer
from .models import CustomUser, Message

class RegisterView(generics.GenericAPIView):
    serializer_class =  UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user=user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'name': user.username
            })
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    serializer_class = EmptySerializer
    permission_class =  [permissions.IsAuthenticated]
    
    def post(self, request):
        if hasattr(request, 'access_token'):
            request.user.access_token.delete()

        return Response({'message': 'User deleted successfully!'}, status=status.HTTP_200_OK)
        