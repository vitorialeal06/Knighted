from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from datetime import datetime
from django.db import models
from .models import Jogador, Partida, Torneio, Abertura, Movimento


def index(request):
    return render(request, 'index.html')


def partida(request):
    return render(request, 'partida.html')


def torneio(request):
    return render(request, 'torneio.html')


def jogador(request):
    return render(request, 'jogador.html')


def abertura(request):
    return render(request, 'abertura.html')


def movimento(request):
    return render(request, 'movimento.html')


def criar_jogador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        nascimento = request.POST.get('nascimento')
        pais = request.POST.get('pais')
        elo = request.POST.get('elo')
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
                return redirect('lista_jogador')
            except ValueError:
                return render(request, 'jogador.html', {'error': 'Data de nascimento inválida.'})
            except Exception as e:
                return render(request, 'jogador.html', {'-type': 'error', 'error': f'Erro ao salvar: {str(e)}'})
        else:
            return render(request, 'jogador.html', {'error': 'Preencha todos os campos.'})
    return render(request, 'jogador.html')


def lista_jogador(request):
    jogadores = Jogador.objects.all()
    return render(request, 'lista_jogador.html', {'jogadores': jogadores})


def remover_jogador(request):
    if request.method == 'POST':
        jogador_id = request.POST.get('jogador_id')
        if not jogador_id:
            return HttpResponseBadRequest("ID do jogador não fornecido")
        jogador = get_object_or_404(Jogador, id_jogador=jogador_id)
        jogador.delete()
        return redirect('lista_jogador')
    return HttpResponseBadRequest("Método não permitido")


def criar_partida(request):
    if request.method == 'POST':
        jogador_brancas_id = request.POST.get('jogador_brancas')
        jogador_pretas_id = request.POST.get('jogador_pretas')
        abertura_brancas_id = request.POST.get('abertura_brancas')
        abertura_pretas_id = request.POST.get('abertura_pretas')
        data_partida = request.POST.get('data_partida')
        duracao = request.POST.get('duracao')
        resultado = request.POST.get('resultado')
        if jogador_brancas_id and jogador_pretas_id and abertura_brancas_id and abertura_pretas_id and data_partida and duracao and resultado:
            try:
                data_partida = datetime.strptime(data_partida, '%Y-%m-%d').date()
                Partida.objects.create(
                    id_jogador_brancas_id=jogador_brancas_id,
                    id_jogador_pretas_id=jogador_pretas_id,
                    id_abertura_brancas_id=abertura_brancas_id,
                    id_abertura_pretas_id=abertura_pretas_id,
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


def remover_partida(request):
    if request.method == 'POST':
        partida_id = request.POST.get('partida_id')
        if not partida_id:
            return HttpResponseBadRequest("ID da partida não fornecido")
        partida = get_object_or_404(Partida, id_partida=partida_id)
        partida.delete()
        return redirect('lista_partida')
    return HttpResponseBadRequest("Método não permitido")


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


def remover_torneio(request):
    if request.method == 'POST':
        torneio_id = request.POST.get('torneio_id')
        if not torneio_id:
            return HttpResponseBadRequest("ID do torneio não fornecido")
        torneio = get_object_or_404(Torneio, id_torneio=torneio_id)
        torneio.delete()
        messages.success(request, 'Torneio removido com sucesso.')
        return redirect('lista_torneio')
    return HttpResponseBadRequest("Método não permitido")


def criar_abertura(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        movimento = request.POST.get('movimento')
        descricao = request.POST.get('descricao')
        if nome and movimento and descricao:
            try:
                Abertura.objects.create(
                    nome=nome,
                    movimento=movimento,
                    descricao=descricao
                )
                return redirect('lista_abertura')
            except Exception as e:
                return render(request, 'abertura.html', {'error': f'Erro ao salvar: {str(e)}'})
        else:
            return render(request, 'abertura.html', {'error': 'Preencha todos os campos obrigatórios.'})
    return render(request, 'abertura.html')


def lista_abertura(request):
    aberturas = Abertura.objects.all()
    return render(request, 'lista_abertura.html', {'aberturas': aberturas})


def remover_abertura(request):
    if request.method == 'POST':
        abertura_id = request.POST.get('abertura_id')
        if not abertura_id:
            return HttpResponseBadRequest("ID da abertura não fornecido")
        abertura = get_object_or_404(Abertura, id_abertura=abertura_id)
        Partida.objects.filter(id_abertura_brancas=abertura).delete()
        Partida.objects.filter(id_abertura_pretas=abertura).delete()
        abertura.delete()
        messages.success(request, 'Abertura removida com sucesso.')
        return redirect('lista_abertura')
    return HttpResponseBadRequest("Método não permitido")


def criar_movimento(request):
    if request.method == 'POST':
        id_partida = request.POST.get('id_partida')
        id_jogador = request.POST.get('id_jogador')
        numero_jogada = request.POST.get('numero_jogada')
        if id_partida and id_jogador and numero_jogada:
            try:
                Movimento.objects.create(
                    id_partida_id=id_partida,
                    id_jogador_id=id_jogador,
                    numero_jogada=numero_jogada
                )
                return redirect('lista_movimento')
            except Exception as e:
                partidas = Partida.objects.all()
                jogadores = Jogador.objects.all()
                return render(request, 'movimento.html', {
                    'error': f'Erro ao salvar: {str(e)}',
                    'partidas': partidas,
                    'jogadores': jogadores
                })
        else:
            partidas = Partida.objects.all()
            jogadores = Jogador.objects.all()
            return render(request, 'movimento.html', {
                'error': 'Preencha todos os campos obrigatórios.',
                'partidas': partidas,
                'jogadores': jogadores
            })
    partidas = Partida.objects.all()
    jogadores = Jogador.objects.all()
    return render(request, 'movimento.html', {
        'partidas': partidas,
        'jogadores': jogadores
    })


def lista_movimento(request):
    movimentos = Movimento.objects.all()
    return render(request, 'lista_movimento.html', {'moviementos': movimentos})


def remover_movimento(request):
    if request.method == 'POST':
        movimento_id = request.POST.get('movimento_id')
        if not movimento_id:
            return HttpResponseBadRequest("ID do movimento não fornecido")
        movimento = get_object_or_404(Movimento, id_movimento=movimento_id)
        try:
            movimento.delete()
            messages.success(request, 'Movimento removido com sucesso.')
        except Exception as e:
            messages.error(request, f'Erro ao remover movimento: {str(e)}')
        return redirect('lista_movimento')
    return HttpResponseBadRequest("Método não permitido")


def relatorio_jogador(request, id_jogador):
    jogador = get_object_or_404(Jogador, id_jogador=id_jogador)

    partidas = Partida.objects.filter(
        models.Q(id_jogador_brancas_id=id_jogador) | models.Q(id_jogador_pretas_id=id_jogador)
    )
    total_partidas = partidas.count()

    vitorias = 0
    empates = 0
    derrotas = 0
    tempo_total = 0
    for partida in partidas:
        if partida.resultado == 'empate':
            empates += 1
        elif partida.resultado == 'brancas' and partida.id_jogador_brancas_id == id_jogador:
            vitorias += 1
        elif partida.resultado == 'pretas' and partida.id_jogador_pretas_id == id_jogador:
            vitorias += 1
        elif partida.resultado == 'brancas' and partida.id_jogador_pretas_id == id_jogador:
            derrotas += 1
        elif partida.resultado == 'pretas' and partida.id_jogador_brancas_id == id_jogador:
            derrotas += 1
        if partida.duracao and partida.duracao.isdigit():
            tempo_total += int(partida.duracao)

    if total_partidas > 0:
        porc_vitorias = (vitorias / total_partidas) * 100
        porc_empates = (empates / total_partidas) * 100
        porc_derrotas = (derrotas / total_partidas) * 100
    else:
        porc_vitorias = porc_empates = porc_derrotas = 0

    horas = tempo_total // 60
    minutos = tempo_total % 60
    tempo_formatado = f"{horas}h {minutos}min" if horas > 0 else f"{minutos}min"

    context = {
        'jogador': jogador,
        'total_partidas': total_partidas,
        'vitorias': vitorias,
        'empates': empates,
        'derrotas': derrotas,
        'porc_vitorias': round(porc_vitorias, 2),
        'porc_empates': round(porc_empates, 2),
        'porc_derrotas': round(porc_derrotas, 2),
        'tempo_total': tempo_formatado,
    }

    return render(request, 'relatorio_jogador.html', context)


def relatorio_torneio(request, id_torneio):
    torneio = get_object_or_404(Torneio, id_torneio=id_torneio)

    partidas = Partida.objects.filter(
        data_partida__range=[torneio.data_inicio, torneio.data_fim]
    )
    total_partidas = partidas.count()

    vitorias_brancas = partidas.filter(resultado='brancas').count()
    vitorias_pretas = partidas.filter(resultado='pretas').count()
    empates = partidas.filter(resultado='empate').count()

    tempo_total = 0
    for partida in partidas:
        if partida.duracao and partida.duracao.isdigit():
            tempo_total += int(partida.duracao)

    horas = tempo_total // 60
    minutos = tempo_total % 60
    tempo_formatado = f"{horas}h {minutos}min" if horas > 0 else f"{minutos}min"

    jogadores_ids = set()
    for partida in partidas:
        if partida.id_jogador_brancas_id:
            jogadores_ids.add(partida.id_jogador_brancas_id)
        if partida.id_jogador_pretas_id:
            jogadores_ids.add(partida.id_jogador_pretas_id)
    jogadores = Jogador.objects.filter(id_jogador__in=jogadores_ids)

    context = {
        'torneio': torneio,
        'total_partidas': total_partidas,
        'vitorias_brancas': vitorias_brancas,
        'vitorias_pretas': vitorias_pretas,
        'empates': empates,
        'tempo_total': tempo_formatado,
        'jogadores': jogadores,
        'total_jogadores': jogadores.count(),
    }

    return render(request, 'relatorio_torneio.html', context)