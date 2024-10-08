from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
import uuid

def homepage(request):
    return render(request, 'pratoservido/homepage.html')

def estabelecimento(request):
    estabelecimentos = Estabelecimento.objects.all()

    context = {'estabelecimentos': estabelecimentos}
    return render(request, 'pratoservido/estabelecimento.html', context)


def cardapio(request, slug=None):
    try:
        estabelecimento = Estabelecimento.objects.get(slug=slug) 
        pratos = estabelecimento.pratos.filter(ativo=True)
    except  Estabelecimento.DoesNotExist:
        return redirect('estabelecimento')
    
    if request.COOKIES.get('id_sessao'):
        id_sessao = request.COOKIES.get('id_sessao')
    else:
        id_sessao = str(uuid.uuid4())
    
    context = {'estabelecimento': estabelecimento, 'pratos': pratos}
    resposta = render(request, 'pratoservido/cardapio.html', context)

    if not request.COOKIES.get('id_sessao'):
        resposta.set_cookie(key='id_sessao', value=id_sessao, max_age=60*60*24*30)

    return resposta


def finalizar_carrinho(request, id_pedido):
    if request.method == 'POST':
        dados = request.POST.dict()
        pedido = Pedido.objects.get(id=id_pedido)
        pedido.forma_pagamento = dados['pagamento']
        pedido.bairro = dados['bairro']
        pedido.endereco = dados['endereco']
        pedido.finalizado = True
        pedido.save()
    

    return redirect('cardapio', slug=pedido.estabelecimento.slug)


@login_required
def administracao(request):
    usuario = request.user
    estabelecimento = Estabelecimento.objects.get(usuario=usuario)
    pedidos = Pedido.objects.filter(estabelecimento=estabelecimento, finalizado=True)

    context = {'estabelecimento': estabelecimento, 'pedidos': pedidos}
    return render(request, 'pratoservido/administracao.html', context)


@login_required
def gerenciar_pratos(request):
    usuario = request.user
    estabelecimento = Estabelecimento.objects.get(usuario=usuario)
    pratos = Prato.objects.filter(estabelecimento=estabelecimento)
    if request.method == 'POST':
        nome = request.POST.get('prato')
        preco = float(request.POST.get('preco'))
        ingredientes = request.POST.get('ingredientes')
        imagem = request.FILES.get('imagem')
        Prato.objects.create(nome=nome, preco=preco, ingredientes=ingredientes, imagem=imagem, estabelecimento=estabelecimento)
        messages.success(request, 'Prato criado com sucesso!')

        return redirect('gerenciar_pratos')
    
    context = {'pratos': pratos}
    return render(request, 'pratoservido/gerenciar_pratos.html', context)


@login_required
def ativar_prato(request, id_prato):
    prato = Prato.objects.filter(id=id_prato).first()

    if not prato:
        messages.warning(request, 'Prato não encontrado!')
        return redirect('gerenciar_pratos')

    if request.method == 'POST':
        prato.ativo = 'ativo' in request.POST
        prato.save()
        messages.success(request, f'Status do prato "{prato.nome}" alterado com sucesso!')

    return redirect('gerenciar_pratos')

@login_required
def remover_prato(request, id_prato):
    prato = Prato.objects.filter(id=id_prato).first()
    
    if not prato:
        messages.warning(request, 'Prato não encontrado!')
        return redirect('gerenciar_pratos')
    
    prato.delete()
    messages.success(request, f'Prato: "{prato.nome}" removido com sucesso!')
    
    return redirect('gerenciar_pratos')


@login_required
def informacoes_estabelecimento(request):
    usuario = request.user
    estabelecimento = Estabelecimento.objects.get(usuario=usuario)
    id = estabelecimento.id

    if request.method == 'POST':
        estabelecimento.nome = request.POST.get('estabelecimento')
        estabelecimento.telefone = request.POST.get('telefone')
        estabelecimento.endereco = request.POST.get('endereco')
        estabelecimento.descricao = request.POST.get('descricao')
        logo = request.FILES.get('logo')
        if logo == None:
            logo = estabelecimento.logo
        else:
            estabelecimento.logo = logo
        estabelecimento.save()
        messages.success(request, 'Informações do estabelecimento alterados com sucesso!')

    context = {'estabelecimento': estabelecimento}
    return render(request, 'pratoservido/informacoes_estabelecimento.html', context)