from django.shortcuts import render
from .models import*
from rest_framework import generics
from .serializers import*
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# views.py
class CustomUserSignUp(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            return Response({'message': 'Inscription réussie', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
        return Response({'message': 'Échec de l\'authentification'}, status=status.HTTP_401_UNAUTHORIZED)

class CustomUserLogout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.auth.delete()  # Supprime le jeton d'authentification de l'utilisateur actuel
        logout(request)
        return Response({'message': 'Déconnexion réussie'}, status=status.HTTP_200_OK)

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer