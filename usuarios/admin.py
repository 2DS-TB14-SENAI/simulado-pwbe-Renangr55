from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario  

# Register your models here.

class UsuarioAdministrator(Usuario ):
    list_display = ('username', 'telefone')
