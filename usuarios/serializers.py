from rest_framework import serializers
from .models import Usuario 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario 
        fields = ['username', 'password', 'telephone']

    def create(self, validated_data):
        usuario = Usuario  .objects.create_user(**validated_data) # validando dados
        usuario.is_active = True #ativando ele
        usuario.save() # salvando
        return usuario
    
    