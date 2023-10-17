from .models import *
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    # owner = serializers.HyperlinkedRelatedField(
    #     view_name='customuser-detail',  # Assurez-vous que le nom de vue est correct
    #     queryset=CustomUser.objects.all(),
    # )
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name']  # Liste des champs requis pour l'inscription
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
