from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros, name='livros'),
    path('api/livros/', view=views.criar_listar_livros),

]