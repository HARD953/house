from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
from django.shortcuts import get_object_or_404
from rest_framework import permissions

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

class EtabliCreate(generics.ListCreateAPIView):
    queryset = Etablissement.objects.all()
    serializer_class = EtabliSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        # Associer l'utilisateur connecté comme propriétaire du Bien
        if self.request.user.is_anonymous:
            serializer.save()
        else:
            serializer.save(auteur=self.request.user)

class EtabliList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EtabliSerializerBien
    def get_queryset(self):
        return Etablissement.objects.filter(auteur=self.request.user)
        
class EtabliDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etablissement.objects.all()
    serializer_class = EtabliSerializer

class ChambreCreate(generics.CreateAPIView):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer

class ChambreList(generics.ListAPIView):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializerl

class ChambreListHotel(generics.ListAPIView):
    serializer_class = ChambreSerializerl
    def get_queryset(self):
        return Chambre.objects.filter(typebien="Hotel")
    
class ChambreListResidence(generics.ListAPIView):
    serializer_class = ChambreSerializerl
    def get_queryset(self):
        return Chambre.objects.filter(typebien="Residence")
         
class ChambreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer


class ReservationCreate(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.all()
    def perform_create(self, serializer):
        chambre_id = self.request.data.get('id_chambre')
        chambre = get_object_or_404(Chambre, pk=chambre_id)
        # Mettez à jour le statut de la chambre
        chambre.disponibilite = True  # Mettez la valeur appropriée selon votre logique
        chambre.save()
        serializer.save()

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class CommentaireList(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class CommentaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class ChambreListAuteur(generics.ListAPIView):
    serializer_class = ChambreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrer les chambres en fonction de l'utilisateur connecté
        return Chambre.objects.filter(auteur=self.request.user)
    
# class TransactionList(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer


# class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
