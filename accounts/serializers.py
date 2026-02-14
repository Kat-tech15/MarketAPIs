from rest_framework import serializers
from .models import CustomUser, Message

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields  = ['id', 'role', 'username', 'password', 'email']
    
    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            password = validated_data['password']
        )
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username =  serializers.CharField()
    password = serializers.CharField()

class EmptySerializer(serializers.Serializer):
    pass

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Message
        fields  = ['id', 'name', 'email', 'message']
