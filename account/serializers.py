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
    
    
    def create(self, validated_data):
        password = validated_data.pop('password')   # removing password from validated data because we will set it using set_password method
        
        user=super().create(validated_data)   # creating user using the remaining validated data
        
        user.set_password(password)   # setting password using set_password method to hash it properly
        
        user.save()   # saving the user instance
        
        return user