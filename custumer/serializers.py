from .models import *
from rest_framework import serializers

class CustomUserSerializerA(serializers.ModelSerializer):
    # owner = serializers.HyperlinkedRelatedField(
    #     view_name='customuser-detail',  # Assurez-vous que le nom de vue est correct
    #     queryset=CustomUser.objects.all(),
    # )
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserSerializerG(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name','numero','pays','profile_image','is_gerant']  # Liste des champs requis pour l'inscription
        extra_kwargs = {'password': {'write_only': True}}  # Pour masquer le mot de passe

    def create(self, validated_data):
        # Créez un nouvel utilisateur avec les données validées
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            numero=validated_data['numero'],
            pays=validated_data['pays'],
            profile_image=validated_data['profile_image'],
            is_gerant=validated_data['is_gerant'],
        )
        return user
    
class CustomUserSerializerP(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name','numero','pays','profile_image','is_propritaire']  # Liste des champs requis pour l'inscription
        extra_kwargs = {'password': {'write_only': True}}  # Pour masquer le mot de passe

    def create(self, validated_data):
        # Créez un nouvel utilisateur avec les données validées
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            numero=validated_data['numero'],
            pays=validated_data['pays'],
            profile_image=validated_data['profile_image'],
            is_propritaire=validated_data['is_propritaire'],
        )
        return user
    
class CustomUserSerializerC(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name','numero','pays','profile_image','is_client']  # Liste des champs requis pour l'inscription
        extra_kwargs = {'password': {'write_only': True}}  # Pour masquer le mot de passe

    def create(self, validated_data):
        # Créez un nouvel utilisateur avec les données validées
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            numero=validated_data['numero'],
            pays=validated_data['pays'],
            profile_image=validated_data['profile_image'],
            is_client=validated_data['is_client'],
        )
        return user
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name','numero','pays','profile_image']  # Liste des champs requis pour l'inscription
        extra_kwargs = {'password': {'write_only': True}}  # Pour masquer le mot de passe

    def create(self, validated_data):
        # Créez un nouvel utilisateur avec les données validées
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user
    
