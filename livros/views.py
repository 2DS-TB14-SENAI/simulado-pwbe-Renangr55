from django.shortcuts import render
from .models import Livro
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import LivroSerializer


# Create your views here.
@api_view(['GET'])
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, "livros.html", {"livros" : livros})


@api_view(['GET','POST'])
def criar_listar_livros (request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
