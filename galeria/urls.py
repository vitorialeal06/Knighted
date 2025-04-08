from django.urls import path
from galeria.views import index, partida, torneio, jogador

urlpatterns = [
    path('', index, name='index'),         
    path('partida/', partida, name='partida'), 
    path('torneio/', torneio, name='torneio'),  
    path('jogador/', jogador, name='jogador'),
]