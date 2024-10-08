from django.shortcuts import render
from .models import *
import uuid


def carrinho(request, id_estabelecimento):
    if request.COOKIES.get('id_sessao'):
        id_sessao = request.COOKIES.get('id_sessao')
    else:
        id_sessao = str(uuid.uuid4())

    cliente, criado = Cliente.objects.get_or_create(id_sessao=id_sessao)
    estabelecimento = Estabelecimento.objects.get(id=id_estabelecimento)
    
    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False, estabelecimento=estabelecimento)
    FORMA_PAGAMENTO_CHOICES = Pedido.FORMA_PAGAMENTO_CHOICES
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)

    context = {'pedido': pedido, 'itens_pedido': itens_pedido, 'forma_pagamento':FORMA_PAGAMENTO_CHOICES}

    resposta = render(request, 'pratoservido/carrinho.html', context)

    if not request.COOKIES.get('id_sessao'):
        resposta.set_cookie(key='id_sessao', value=id_sessao, max_age=60*60*24*30)

    return resposta


def add_carrinho(request, id_prato):
    if request.method == 'POST':
        id_sessao = request.COOKIES.get('id_sessao')
        cliente, criado = Cliente.objects.get_or_create(id_sessao=id_sessao)
        prato = Prato.objects.get(id=id_prato)
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False, estabelecimento=prato.estabelecimento)
        FORMA_PAGAMENTO_CHOICES = Pedido.FORMA_PAGAMENTO_CHOICES

        item_pedido, criado = ItensPedido.objects.get_or_create(prato=prato, pedido=pedido)
        item_pedido.quantidade += 1
        item_pedido.save()

        itens_pedido = ItensPedido.objects.filter(pedido=pedido)
        context = {'itens_pedido':itens_pedido, 'pedido': pedido, 'forma_pagamento': FORMA_PAGAMENTO_CHOICES}

    return render(request, 'pratoservido/carrinho.html', context) 


def remover_carrinho(request, id_prato):
    if request.method == 'POST':
        id_sessao = request.COOKIES.get('id_sessao')
        cliente, criado = Cliente.objects.get_or_create(id_sessao=id_sessao)
        prato = Prato.objects.get(id=id_prato)
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False, estabelecimento=prato.estabelecimento)
        FORMA_PAGAMENTO_CHOICES = Pedido.FORMA_PAGAMENTO_CHOICES

        item_pedido, criado = ItensPedido.objects.get_or_create(prato=prato, pedido=pedido)
        item_pedido.quantidade -= 1
        if item_pedido.quantidade <= 0:
            item_pedido.delete()
        else:
            item_pedido.save()

        itens_pedido = ItensPedido.objects.filter(pedido=pedido)
        context = {'itens_pedido':itens_pedido, 'pedido': pedido, 'forma_pagamento': FORMA_PAGAMENTO_CHOICES}

    return render(request, 'pratoservido/carrinho.html', context)


def excluir_carrinho(request, id_prato):
    if request.method == 'POST':
        id_sessao = request.COOKIES.get('id_sessao')
        cliente, criado = Cliente.objects.get_or_create(id_sessao=id_sessao)
        prato = Prato.objects.get(id=id_prato)
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False, estabelecimento=prato.estabelecimento)
        FORMA_PAGAMENTO_CHOICES = Pedido.FORMA_PAGAMENTO_CHOICES

        item_pedido, criado = ItensPedido.objects.get_or_create(prato=prato, pedido=pedido)
        item_pedido.delete()
       
        itens_pedido = ItensPedido.objects.filter(pedido=pedido)
        context = {'itens_pedido':itens_pedido, 'pedido': pedido, 'forma_pagamento': FORMA_PAGAMENTO_CHOICES}

    return render(request, 'pratoservido/carrinho.html', context)