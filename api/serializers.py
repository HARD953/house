from .models import *
from custumer.models import *
from rest_framework import serializers

class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'equipement-detail'},  # Remplacez 'equipement-detail' par le nom correct de votre vue
        }

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'service-detail'},  # Remplacez 'service-detail' par le nom correct de votre vue
        }

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'reservation-detail'},  # Remplacez 'reservation-detail' par le nom correct de votre vue
        }

class CommentaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'commentaire-detail'},  # Remplacez 'commentaire-detail' par le nom correct de votre vue
        }


class ChambreSerializer(serializers.ModelSerializer):
    # bien = serializers.HyperlinkedRelatedField(
    #     view_name='bien-detail',  # Remplacez 'chambre-detail' par le nom correct de votre vue
    #     queryset=Bien.objects.all()
    # )
    class Meta:
        model = Chambre 
        fields = '__all__'
        # extra_kwargs = {
        #     'url': {'view_name': 'chambre-detail'},  # Remplacez 'chambre-detail' par le nom correct de votre vue
        # }
class EtabliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etablissement 
        fields = '__all__'

class EtabliSerializerBien(serializers.ModelSerializer):
    class Meta:
        model = Etablissement 
        fields = ['auteur','typebien','nom']

class ChambreSerializerl(serializers.ModelSerializer):
    class Meta:
        model = Chambre 
        fields = ['typebien','nombien','nomchambre','commune','etoile','prix','img1']


# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Image
#         fields = '__all__'
#         extra_kwargs = {
#             'url': {'view_name': 'image-detail'},  # Remplacez 'image-detail' par le nom correct de votre vue
#         }





# class ChambreListSerializer(serializers.HyperlinkedModelSerializer):
#     # bien = serializers.HyperlinkedRelatedField(
#     #     view_name='bien-detail',  # Remplacez 'chambre-detail' par le nom correct de votre vue
#     #     queryset=Bien.objects.all()
#     # )
#     class Meta:
#         model = Chambre
#         fields = ['capacitelits', 'images']
#         extra_kwargs = {
#             'url': {'view_name': 'chambre-detail'},  # Remplacez 'chambre-detail' par le nom correct de votre vue
#         }

# class ChambreBienSerializer(serializers.ModelSerializer):
#     # bien = serializers.HyperlinkedRelatedField(
#     #     view_name='bien-detail',  # Remplacez 'chambre-detail' par le nom correct de votre vue
#     #     queryset=Bien.objects.all()
#     # )  # Pour afficher les détails du bien
#     # bien = serializers.StringRelatedField()
#     class Meta:
#         model = Chambre
#         fields = ['id','prix','type','region','etoile','img1','img2','img3','img4','img5']
#         extra_kwargs = {
#             'url': {'view_name': 'chambre-detail'},  # Remplacez 'chambre-detail' par le nom correct de votre vue
#         }

# class BienSerializer(serializers.HyperlinkedModelSerializer):
#     equipements = EquipementSerializer(many=True, read_only=True)

#     class Meta:
#         model = Bien
#         fields = '__all__'
#         extra_kwargs = {
#             'url': {'view_name': 'bien-detail'},  # Remplacez 'bien-detail' par le nom correct de votre vue
#         }
                                                                                            

# class TransactionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = '__all__'
#         extra_kwargs = {
#             'url': {'view_name': 'transaction-detail'},  # Remplacez 'transaction-detail' par le nom correct de votre vue
#         }

# Faites de même pour les autres serializers en ajustant les noms de vue selon votre configuration.
