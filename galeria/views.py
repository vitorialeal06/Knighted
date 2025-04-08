from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def partida(request):
    return render(request, 'partida.html')

def torneio(request):
    return render(request, 'torneio.html')

def jogador(request):
    return render(request, 'jogador.html')