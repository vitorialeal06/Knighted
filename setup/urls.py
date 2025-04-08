from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import os
from galeria.views import index, partida, torneio, jogador

urlpatterns = [
    path('', index, name='index'),
    path('partida/', partida, name='partida'),
    path('torneio/', torneio, name='torneio'),
    path('jogador/', jogador, name='jogador'),
]

# Serve arquivos estáticos em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'galeria/assets'))
    # Se também usar setup/static, adicione:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'setup/static'))