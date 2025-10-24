from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    
    
    email = serializers.EmailField(max_length=255, required=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, required=True, min_length=8) 

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate(self,attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        
        if email_exists:
            raise ValidationError({'email':'Email is already in use'})
        
        
        return super().validate(attrs)