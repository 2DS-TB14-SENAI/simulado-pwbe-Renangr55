from django.shortcuts import render
from .models import Usuario , AbstractUser
from .serializers import UsuarioSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['POST'])
def criarUsuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)


    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'acess' : str(refresh.access_token),
            'refresh' : str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro' : 'usuario ou senha invalidos'}, status=status.HTTP_401_UNAUTHORIZED)

