from rest_framework import serializers
from .models import User
from django.utils import timezone

# --- Serializer for user registration ---
class UserRegistrationSerializer(serializers.ModelSerializer):
    '''
    Model is used to define Which database table to use
    Which model to serialize
    Which fields to include
    How to behave internally

    class Meta is used to provide configuration for Django models, serializers, and forms.
    It tells Django/DRF things like which model to use, which fields to include, ordering, database table name, etc.
    It is like a settings section inside the class.
    '''
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data['email']
        local_part = email.split("@")[0]
        user = User.objects.create_user(
            email=email,
            username=local_part,
            password=validated_data['password']
        )
        return user
    
# --- Serializer to return user details ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')