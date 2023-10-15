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