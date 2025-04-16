from django.urls import path
from . import views
from galeria.views import index, partida, torneio, jogador

urlpatterns = [
    path('', index, name='index'),   
     path('', views.index, name='index'),      
    path('partida/', partida, name='partida'), 
    path('torneio/', torneio, name='torneio'),  
    path('jogador/', jogador, name='jogador'),
    path('criarJogador/', views.criar_jogador, name='criar_jogador'),
    path('listaJogadores/', views.lista_jogadores, name='lista_jogadores'),
    path('criarPartida/', views.criar_partida, name='criar_partida'),
    path('listaPartida/', views.lista_partida, name='lista_partida'),
    path('criarTorneio/', views.criar_torneio, name='criar_torneio'),
    path('listaTorneio/', views.lista_torneio, name='lista_torneio'),
]