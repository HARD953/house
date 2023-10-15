from rest_framework import generics
from .models import Equipement, Service, Image, Bien, Chambre, Reservation, Commentaire, Transaction
from .serializers import *




class EquipementList(generics.ListCreateAPIView):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer

class EquipementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class BienList(generics.ListCreateAPIView):
    queryset = Bien.objects.all()
    serializer_class = BienSerializer

class BienDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bien.objects.all()
    serializer_class = BienSerializer

class ChambreList(generics.ListCreateAPIView):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer

class ChambreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class CommentaireList(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class CommentaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
