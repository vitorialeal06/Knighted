from django.urls import path
from . import views
from galeria.views import index, partida, torneio, jogador, abertura, movimento

urlpatterns = [
    path('', index, name='index'),   
     path('', views.index, name='index'),      
    path('partida/', partida, name='partida'), 
    path('torneio/', torneio, name='torneio'),  
    path('jogador/', jogador, name='jogador'),
    path('abertura/', abertura, name='abertura'),
    path('movimento/', movimento, name='movimento'),

    path('Jogador/criar/', views.criar_jogador, name='criar_jogador'),
    path('Jogadores/lista/', views.lista_jogadores, name='lista_jogadores'),
    path('Partida/criar/', views.criar_partida, name='criar_partida'),
    path('Partida/lista/', views.lista_partida, name='lista_partida'),
    path('Torneio/criar/', views.criar_torneio, name='criar_torneio'),
    path('Torneio/lista/', views.lista_torneio, name='lista_torneio'),
    path('Abertura/criar', views.criar_abertura, name='criar_abertura'),
    path('Abertura/lista/', views.lista_abertura, name='lista_abertura'),
    path('Movimento/criar/', views.criar_movimento, name='criar_movimento'),
    path('Movimento/lista/', views.lista_movimento, name='lista_movimento'),
]