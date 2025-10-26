from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from rest_framework import generics,status

from rest_framework.response import Response
from .models import User

from rest_framework.request import Request
from rest_framework.views import APIView
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    
    
    def post(self,request:Request):
        data=request.data
        
        serializer=self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            
            response={
                'message':'User created successfully',
                'user':serializer.data
            }
            
            
            return Response(data=response,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    
#  difference between APIView and GenericAPIView is that GenericAPIView provides built in methods like get_serializer, get_queryset etc which are not present in APIView
# in api view we have to define everything from scratch
class LoginView(APIView):
    
    
    
    def post(self,request:Request):
        
        email=request.data.get('email')
        
        password=request.data.get('password')
        
        
        
        
    def get(self,request:Request):
        content={'user':str(request.user),'auth':str(request.auth)}
        
        
        return Response(data=content,status=status.HTTP_200_OK)