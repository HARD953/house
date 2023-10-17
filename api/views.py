from rest_framework import generics
from .models import Equipement, Service, Image, Bien, Chambre, Reservation, Commentaire, Transaction
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class EquipementList(generics.ListCreateAPIView):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer
@csrf_exempt
class EquipementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer
@csrf_exempt
class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
@csrf_exempt
class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
@csrf_exempt
class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
@csrf_exempt
class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
@csrf_exempt
class BienCreate(generics.CreateAPIView):
    queryset = Bien.objects.all()
    serializer_class = BienSerializer
    def perform_create(self, serializer):
        # Associer l'utilisateur connecté comme propriétaire du Bien
        serializer.save(owner=self.request.user)
@csrf_exempt
class BienList(generics.ListAPIView):
    serializer_class = BienSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filtrer les objets Bien pour l'utilisateur connecté
            return Bien.objects.filter(owner=self.request.user)
        else:
            # Renvoyer tous les objets Bien si personne n'est connecté
            return Bien.objects.all()
 @csrf_exempt       
class BienDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BienSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filtrer les objets Bien pour l'utilisateur connecté
            return Bien.objects.filter(owner=self.request.user)
        else:
            # Renvoyer tous les objets Bien si personne n'est connecté
            return Bien.objects.all()
@csrf_exempt       
class ChambreCreate(generics.CreateAPIView):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer
    def perform_create(self, serializer):
        # Associer l'utilisateur connecté comme propriétaire du Chambre
        serializer.save(owner=self.request.user)

@csrf_exempt
class ChambreList(generics.ListAPIView):
    serializer_class = ChambreSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filtrer les objets Chambre pour l'utilisateur connecté
            return Chambre.objects.filter(owner=self.request.user)
        else:
            # Renvoyer tous les objets Chambre si personne n'est connecté
            return Chambre.objects.all()

@csrf_exempt        
class ChambreDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChambreSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filtrer les objets Chambre pour l'utilisateur connecté
            return Chambre.objects.filter(owner=self.request.user)
        else:
            # Renvoyer tous les objets Chambre si personne n'est connecté
            return Chambre.objects.all()

@csrf_exempt
class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

@csrf_exempt
class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

@csrf_exempt
class CommentaireList(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

@csrf_exempt
class CommentaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

@csrf_exempt
class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

@csrf_exempt
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
