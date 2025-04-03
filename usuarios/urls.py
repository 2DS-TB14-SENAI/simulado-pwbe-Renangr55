from django.urls import path
from . import views

urlpatterns = [
    path('auth/registro/', view=views.criarUsuario),
    path('auth/login/', view=views.logar)
]