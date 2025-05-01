from django.urls import path
from . import views
from galeria.views import index, partida, torneio, jogador, abertura, movimento

urlpatterns = [
    path('', views.index, name='index'),  # Path duplicado
    path('Partida/', views.partida, name='partida'),
    path('Torneio/', views.torneio, name='torneio'),
    path('Jogador/', views.jogador, name='jogador'),
    path('Abertura/', views.abertura, name='abertura'),
    path('Movimento/', views.movimento, name='movimento'),
    path('Jogador/criar/', views.criar_jogador, name='criar_jogador'),
    path('Jogador/lista/', views.lista_jogador, name='lista_jogador'),
    path('Jogador/remover/', views.remover_jogador, name='remover_jogador'),
    path('Partida/criar/', views.criar_partida, name='criar_partida'),
    path('Partida/lista/', views.lista_partida, name='lista_partida'),
    path('Partida/remover/', views.remover_partida, name='remover_partida'),
    path('Torneio/criar/', views.criar_torneio, name='criar_torneio'),
    path('Torneio/lista/', views.lista_torneio, name='lista_torneio'),
    path('Torneio/remover/', views.remover_torneio, name='remover_torneio'),
    path('Abertura/criar/', views.criar_abertura, name='criar_abertura'),  # Barra faltando
    path('Abertura/lista/', views.lista_abertura, name='lista_abertura'),
    path('Abertura/remover/', views.remover_abertura, name='remover_abertura'),
    path('Movimento/criar/', views.criar_movimento, name='criar_movimento'),
    path('Movimento/lista/', views.lista_movimento, name='lista_movimento'),
    path('Movimento/remover/', views.remover_movimento, name='remover_movimento'),
    # Nova URL para o relatório
    path('Jogador/relatorio/<int:id_jogador>/', views.relatorio_jogador, name='relatorio_jogador'),
    path('Torneio/relatorio/<int:id_torneio>/', views.relatorio_torneio, name='relatorio_torneio'),
]