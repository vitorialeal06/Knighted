from django.shortcuts import render, redirect
from .models import Jogador, Partida, Abertura, Torneio
from django.contrib import messages 
from datetime import datetime

def index(request): #retornar a pg
    return render(request, 'index.html')

def partida(request):
    return render(request, 'partida.html')

def torneio(request):
    return render(request, 'torneio.html')

def jogador(request):
    return render(request, 'jogador.html')


def criar_jogador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        nascimento = request.POST.get('nascimento')
        pais = request.POST.get('pais')
        elo = request.POST.get('elo')

        # Validação
        if nome and nascimento and pais and elo:
            if len(nome) > 100:
                return render(request, 'jogador.html', {'error': 'Nome muito longo (máx. 100 caracteres).'})
            if len(pais) > 25:
                return render(request, 'jogador.html', {'error': 'País muito longo (máx. 25 caracteres).'})
            try:
                nascimento = datetime.strptime(nascimento, '%Y-%m-%d').date()
                Jogador.objects.create(
                    nome=nome,
                    data_nascimento=nascimento,
                    pais=pais,
                    elo=elo
                )
                return redirect('lista_jogadore')
            except ValueError:
                return render(request, 'jogador.html', {'error': 'Data de nascimento inválida.'})
            except Exception as e:
                return render(request, 'jogador.html', {'-type': 'error', 'error': f'Erro ao salvar: {str(e)}'})
        else:
            return render(request, 'jogador.html', {'error': 'Preencha todos os campos.'})
    return render(request, 'jogador.html')

def lista_jogadores(request):
    jogadores = Jogador.objects.all()
    return render(request, 'lista_jogador.html', {'jogadores': jogadores})


def criar_partida(request):
    if request.method == 'POST':
        jogador_brancas_id = request.POST.get('jogador_brancas')
        jogador_pretas_id = request.POST.get('jogador_pretas')
        abertura_id = request.POST.get('abertura')
        data_partida = request.POST.get('data_partida')
        duracao = request.POST.get('duracao')
        resultado = request.POST.get('resultado')
        if jogador_brancas_id and jogador_pretas_id and abertura_id and data_partida and resultado:
            try:
                data_partida = datetime.strptime(data_partida, '%Y-%m-%d').date()
                duracao = datetime.strptime(duracao, '%Y-%m-%dT%H:%M') if duracao else None
                Partida.objects.create(
                    id_jogador_brancas_id=jogador_brancas_id,
                    id_jogador_pretas_id=jogador_pretas_id,
                    id_abertura_id=abertura_id,
                    data_partida=data_partida,
                    duracao=duracao,
                    resultado=resultado
                )
                return redirect('lista_partida')
            except ValueError:
                return render(request, 'partida.html', {
                    'error': 'Data ou duração inválida.',
                    'jogadores': Jogador.objects.all(),
                    'aberturas': Abertura.objects.all()
                })
            except Exception as e:
                return render(request, 'partida.html', {
                    'error': f'Erro ao salvar: {str(e)}',
                    'jogadores': Jogador.objects.all(),
                    'aberturas': Abertura.objects.all()
                })
        else:
            return render(request, 'partida.html', {
                'error': 'Preencha todos os campos obrigatórios.',
                'jogadores': Jogador.objects.all(),
                'aberturas': Abertura.objects.all()
            })
    return render(request, 'partida.html', {
        'jogadores': Jogador.objects.all(),
        'aberturas': Abertura.objects.all()
    })

def lista_partida(request):
    partidas = Partida.objects.all()
    return render(request, 'lista_partida.html', {'partidas': partidas})

def criar_torneio(request):
    if request.method == 'POST':
        nome_torneio = request.POST.get('nome_torneio')
        localizacao = request.POST.get('localizacao')
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        if nome_torneio and localizacao and data_inicio and data_fim:
            try:
                data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
                data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
                Torneio.objects.create(
                    nome_torneio=nome_torneio,
                    localizacao=localizacao,
                    data_inicio=data_inicio,
                    data_fim=data_fim
                )
                return redirect('lista_torneio')
            except ValueError:
                return render(request, 'torneio.html', {'error': 'Datas inválidas.'})
            except Exception as e:
                return render(request, 'torneio.html', {'error': f'Erro ao salvar: {str(e)}'})
        else:
            return render(request, 'torneio.html', {'error': 'Preencha todos os campos.'})
    return render(request, 'torneio.html')

def lista_torneio(request):
    torneios = Torneio.objects.all()
    return render(request, 'lista_torneio.html', {'torneios': torneios})