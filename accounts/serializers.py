from rest_framework import serializers
from .models import CustomUser, Message

class UserSerializer(serializers.ModelSerializer):
    otp_via = serializers.ChoiceField(
        choices=[('email', 'Email'), ('sms', 'SMS')],
        default='email',
        write_only=True
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields  = ['id', 'role', 'username', 'password', 'email', 'otp_via']
    
    def create(self, validated_data):
        otp_via = validated_data.pop('otp_via', 'email')
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        user.otp_via = otp_via
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

class VerifyOTPSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

class ResendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
